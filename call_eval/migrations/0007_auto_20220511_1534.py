# Generated by Django 3.2.13 on 2022-05-11 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call_eval', '0006_souscriterescore_souscritere'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criterescore',
            name='critere',
        ),
        migrations.RemoveField(
            model_name='criterescore',
            name='reportcall',
        ),
        migrations.RemoveField(
            model_name='reportcall',
            name='call',
        ),
        migrations.RemoveField(
            model_name='souscriterescore',
            name='sousCritere',
        ),
    ]
