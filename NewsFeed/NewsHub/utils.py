from functools import wraps

from NewsHub.exceptions import ClientError
from NewsHub.models import WorldData


def catch_client_error(func):
    @wraps(func)
    def inner(message, *args, **kwrargs):
        try:
            return func(message, *args, **kwrargs)
        except ClientError as e:
            e.send_to(message.reply_channel)

    return inner


def get_world_or_error(world_id, user):
    if not user.is_authenticated:
        raise ClientError("USER_HAS_TO_LOGIN")
    try:
        world = WorldData.objects.get(pk=world_id)
    except WorldData.DoesNotExist:
        raise ClientError("get_world_or_error: WorldData.DoesNotExist")
    return world
