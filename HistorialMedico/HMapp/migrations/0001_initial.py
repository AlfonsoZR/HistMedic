# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilMedico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateTimeField()),
                ('tipoSangre', models.TextField()),
            ],
        ),
    ]
