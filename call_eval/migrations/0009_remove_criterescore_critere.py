# Generated by Django 3.2.13 on 2022-05-11 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call_eval', '0008_auto_20220511_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criterescore',
            name='critere',
        ),
    ]