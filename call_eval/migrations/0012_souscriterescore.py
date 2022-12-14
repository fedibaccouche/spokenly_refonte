# Generated by Django 3.2.13 on 2022-05-12 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('call_eval', '0011_delete_souscriterescore'),
    ]

    operations = [
        migrations.CreateModel(
            name='SousCritereScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=100, null=True)),
                ('criterescore', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='call_eval.criterescore')),
                ('sousCritere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='call_eval.souscritere')),
            ],
        ),
    ]
