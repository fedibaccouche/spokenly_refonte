# Generated by Django 3.2.13 on 2022-05-11 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call_eval', '0004_auto_20220510_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='souscriterescore',
            name='sousCritere',
        ),
    ]
