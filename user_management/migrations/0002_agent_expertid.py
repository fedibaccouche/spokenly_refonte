# Generated by Django 3.2.13 on 2022-04-27 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='expertid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.expert'),
            preserve_default=False,
        ),
    ]
