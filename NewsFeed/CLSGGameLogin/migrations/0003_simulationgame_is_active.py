# Generated by Django 2.0b1 on 2017-10-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLSGGameLogin', '0002_simulationgame_game_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationgame',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
