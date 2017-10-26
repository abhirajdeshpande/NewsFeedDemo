from channels.auth import channel_session_user_from_http, channel_session_user

from NewsHub.exceptions import ClientError
from NewsHub.models import WorldData
from channels import Channel
import json

from NewsHub.utils import catch_client_error, get_destination_or_error


# take user from the http and insert in the channel_session
# makes user available in the message.user attribute
@channel_session_user_from_http
def ws_connect(message):
    message.reply_channel.send({"accept": True})
    message.channel_session['worlds'] = []


@channel_session_user
def ws_disconnect(message):
    # Unsubscribe from any connected world
    for world_id in message.channel_session.get("worlds", set()):
        try:
            world = WorldData.objects.get(pk=world_id)
            # removes from the world's send group
            # if this doesn't work, then removes once the first reply message
            #  expires
            world.websocket_group.discard(message.reply_channel)
        except WorldData.DoesNotExist:
            print("Exception: World does not exist")


def ws_receive(message):
    payload = json.loads(message['text'])
    # print("ws_receive(message) " + message['text'])
    payload['reply_channel'] = message.content['reply_channel']
    Channel("NewsHub.receive").send(payload)


@channel_session_user
@catch_client_error
def world_join(message):
    # Find the world they requested (by ID)
    world = get_destination_or_error(message)

    print("Welcome to the world!")

    # add them in
    world.websocket_group.add(message.reply_channel)
    message.channel_session['worlds'] = list(set(message.channel_session[
                                                     'worlds']).union(
        [world.id]))

    # Send a message back that will prompt them to open the world
    message.reply_channel.send({
        "text": json.dumps({
            "join": str(world.id),
            "title": world.world_name,
        })
    })


@channel_session_user
@catch_client_error
def world_leave(message):
    # Find the world they requested (by ID)
    world = get_destination_or_error(message)

    print("See you soon!")

    # add them in
    world.websocket_group.discard(message.reply_channel)
    message.channel_session['worlds'] = list(set(message.channel_session[
                                                     'worlds']).union(
        [world.id]))

    # Send a message back that will prompt them to close the world
    message.reply_channel.send({
        "text": json.dumps({
            "leave": str(world.id),
        })
    })


@channel_session_user
@catch_client_error
def news_publish(message):
    if str(int(message['world'])) not in message.channel_session['worlds']:
        raise ClientError("WORLD_ACCESS_DENIED")

    # print("Here's something about the world!")

    world = get_destination_or_error(message)
    world.send_message(message)
