from functools import wraps

from NewsHub.exceptions import ClientError
from NewsHub.models import WorldNewsCenterClass


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
        world = WorldNewsCenterClass.objects.get(pk=world_id)
    except WorldNewsCenterClass.DoesNotExist:
        raise ClientError("ROOM_INVALID")
    return world
