# Generated by Django 2.0b1 on 2017-10-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLSGGameLogin', '0003_simulationgame_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationgame',
            name='details',
            field=models.CharField(blank=True, max_length=5120),
        ),
    ]
