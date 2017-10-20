import json

from django.db import models
from django.utils.six import python_2_unicode_compatible
from channels import Group

# Create your models here.
from djchoices import DjangoChoices, ChoiceItem


@python_2_unicode_compatible
class UserClass(models.Model):
    """
    User information
    """

    # Enumerators
    class EnumUserRole(DjangoChoices):
        roleA = ChoiceItem("Role A")
        roleB = ChoiceItem("Role B")
        roleC = ChoiceItem("Role C")
        roleD = ChoiceItem("Role D")
        roleE = ChoiceItem("Role E")

    class EnumUserCountry(DjangoChoices):
        countryA = ChoiceItem("Country A")
        countryB = ChoiceItem("Country B")
        countryC = ChoiceItem("Country C")
        countryD = ChoiceItem("Country D")

    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    world = models.CharField(max_length=255)
    role = models.CharField(max_length=1, choices=EnumUserRole.choices)
    country = models.CharField(max_length=1, choices=EnumUserCountry.choices)

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class NewsClass(models.Model):
    """
    News that are shown in the news feed
    """
    time = models.DateTimeField()
    summary = models.CharField(max_length=512)
    content = models.CharField(max_length=4096)
    isLink = models.BooleanField(default=False)
    user = UserClass

    def __str__(self):
        return self.summary


@python_2_unicode_compatible
class WorldNewsCenterClass(models.Model):
    """
    Center for people to subscribe to news
    """
    news_center_name = models.CharField(max_length=255)

    def __str__(self):
        return self.news_center_name

    @property
    def websocket_group(self):
        """
        Returns the channels group that sockets should subscribe to, to get news as
        they are generated
        """
        return Group("world-%s" % self.id)

    def send_message(self, message, user):
        final_msg = {
            'world': str(self.id),
            'News': message[0],
            # 'content': message.content,
            'username': user.username,
            'Time': message[1],
            # 'isLink': message.isLink,
        }

        # print("send_message")

        self.websocket_group.send({
            "text": json.dumps(final_msg)
        })
