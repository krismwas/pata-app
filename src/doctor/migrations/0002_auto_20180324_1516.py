# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-24 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='doctor',
            field=models.BooleanField(default=False),
        ),
    ]
