# Generated by Django 2.0b1 on 2017-10-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsHub', '0010_auto_20171024_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userclass',
            name='country',
            field=models.CharField(choices=[('country_A', 'country_A'), ('country_B', 'country_B'), ('country_C', 'country_C'), ('country_D', 'country_D')], max_length=30),
        ),
        migrations.AlterField(
            model_name='userclass',
            name='role',
            field=models.CharField(choices=[('Role A', 'Role A')], max_length=30),
        ),
        migrations.AlterField(
            model_name='userclass',
            name='world',
            field=models.CharField(choices=[('tempWorld', 'tempWorld')], max_length=30),
        ),
    ]
