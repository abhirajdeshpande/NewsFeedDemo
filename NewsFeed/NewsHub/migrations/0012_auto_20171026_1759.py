# Generated by Django 2.0b1 on 2017-10-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsHub', '0011_auto_20171026_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userclass',
            name='country',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userclass',
            name='role',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userclass',
            name='world',
            field=models.CharField(max_length=30),
        ),
    ]