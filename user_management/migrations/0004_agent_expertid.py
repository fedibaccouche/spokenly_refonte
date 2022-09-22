# Generated by Django 3.2.13 on 2022-05-06 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_remove_agent_expertid'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='expertid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.expert'),
            preserve_default=False,
        ),
    ]
