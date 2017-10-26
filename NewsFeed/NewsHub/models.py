import json

from django.conf import settings
from django.db import models
from django.utils.six import python_2_unicode_compatible
from channels import Group
from django.contrib.auth.models import AbstractUser

from CLSGGameLogin.models import SimulationGame

from multiselectfield import MultiSelectField


# Create your models here.

@python_2_unicode_compatible
class WorldData(models.Model):
    world_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    running = models.BooleanField(default=False)
    lastday = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = 'WorldData'
        verbose_name_plural = "world data"

    def __str__(self):
        return self.world_name

    @property
    def websocket_group(self):
        """
        Returns the channels group that sockets should subscribe to, to get news as
        they are generated
        """
        return Group("world-%s" % self.id)

    def send_message(self, message):
        final_msg = {
            'world': message['world'],
            'country': message['country'],
            'role': message['role'],
            'summary': message['summary'],
            'content': message['content'],
            'time': message['time'],
            'isLink': message['isLink'],
        }

        print("send_message" + str(message.user.role) + message['role'])

        self.websocket_group.send({
            "text": json.dumps(final_msg)
        })


class CountryData(models.Model):
    world = models.ForeignKey('WorldData', on_delete=models.CASCADE, )
    country = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=128)  # slugify(world_name) + "_" + slugify(country)
    S = models.TextField()  # holds stringified dictionary of array
    E = models.TextField()  # holds stringified dictionary of array
    IsoS = models.TextField()  # holds stringified dictionary of array
    Iso = models.TextField()  # holds stringified dictionary of array
    Q = models.TextField()  # holds stringified dictionary of array
    I = models.TextField()  # holds stringified dictionary of array
    T = models.TextField()  # holds stringified dictionary of array
    Rec = models.TextField()  # holds stringified dictionary of array
    D = models.TextField()  # holds stringified dictionary of array
    V = models.TextField()  # holds stringified dictionary of array
    Rm = models.TextField()  # holds stringified dictionary of array
    N = models.TextField()  # holds stringified dictionary of array
    susc2exp = models.TextField()  # holds stringified dictionary of array
    exp2infec = models.TextField()  # holds stringified dictionary of array
    rec2susc = models.TextField()  # holds stringified dictionary of array
    exp2iso = models.TextField()  # holds stringified dictionary of array
    isoinfec2quar = models.TextField()  # holds stringified dictionary of array
    infec2rec = models.TextField()  # holds stringified dictionary of array
    rx2rec = models.TextField()  # holds stringified dictionary of array
    infec2rx = models.TextField()  # holds stringified dictionary of array
    quar2rx = models.TextField()  # holds stringified dictionary of array
    susc2rec = models.TextField()  # holds stringified dictionary of array
    infecquar2died = models.TextField()  # holds stringified dictionary of array

    class Meta:
        managed = True
        db_table = 'CountryData'
        verbose_name_plural = "country data"

    def __str__(self):
        return self.slug


class RoleData(models.Model):
    world = models.ForeignKey('WorldData', on_delete=models.CASCADE, )
    country = models.CharField(max_length=64)
    role = models.CharField(max_length=64)
    slug = models.SlugField(
        max_length=200)  # slugify(world_name) + "_" + slugify(country_A) + "_" + slugify(role)

    class Meta:
        managed = True
        db_table = 'RoleData'
        verbose_name_plural = "role data"

    def __str__(self):
        return self.slug


def get_games_list():
    games = SimulationGame.objects.all().values_list('game_name', flat=True)
    games_list = list(zip(games, games))
    return games_list


def get_worlds_list():
    worlds = WorldData.objects.all().values_list('world_name', flat=True)
    world_ids = WorldData.objects.all().values_list('id', flat=True)
    worlds_list = list(zip(world_ids, worlds))
    return worlds_list


def get_country_list():
    countries = CountryData.objects.all().values_list('country', flat=True)
    country_id = CountryData.objects.all().values_list('id', flat=True)
    countries_list = list(zip(country_id, countries))
    return countries_list


def get_roles_list():
    roles = RoleData.objects.all().values_list('role', flat=True)
    role_id = RoleData.objects.all().values_list('id', flat=True)
    roles_list = list(zip(role_id, roles))
    return roles_list


@python_2_unicode_compatible
class UserClass(AbstractUser):
    """
    User information
    """

    world = models.CharField(max_length=10, choices=get_worlds_list())
    role = models.CharField(max_length=10, choices=get_roles_list())
    country = models.CharField(max_length=10, choices=get_country_list())

    allowed_games = MultiSelectField(choices=get_games_list())

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class NewsClass(models.Model):
    """
    News that are shown in the news feed
    """
    time = models.DateTimeField()
    summary = models.CharField(max_length=512)
    content = models.CharField(max_length=4096)
    isLink = models.BooleanField(default=False)
    user = UserClass(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.summary
