# Generated by Django 3.2.13 on 2022-04-27 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_agent_expertid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='expertid',
        ),
    ]
