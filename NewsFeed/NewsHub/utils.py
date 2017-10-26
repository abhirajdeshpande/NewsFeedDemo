from functools import wraps

from NewsHub.exceptions import ClientError
from NewsHub.models import WorldData, get_country_list, get_roles_list


def catch_client_error(func):
    @wraps(func)
    def inner(message, *args, **kwrargs):
        try:
            return func(message, *args, **kwrargs)
        except ClientError as e:
            # e.send_to(message.reply_channel)
            print(e)

    return inner


def get_destination_or_error(message):
    if not message.user.is_authenticated:
        raise ClientError("USER_HAS_TO_LOGIN")
    try:
        if message['command'] == 'send':

            country_dict = dict(get_country_list())
            role_dict = dict(get_roles_list())

            if country_dict[str(message.user.country)] == message['country'] \
                    and role_dict[str(message.user.role)] == message['role']:
                world = WorldData.objects.get(pk=message['world'])
            else:
                raise ClientError("NOT_FOR_USER: " + country_dict[str(
                    message.user.country)] + "\t" + role_dict[
                                      str(message.user.role)])
        else:
            world = WorldData.objects.get(pk=message['world'])

    except WorldData.DoesNotExist:
        raise ClientError("get_world_or_error: WorldData.DoesNotExist")
    return world
