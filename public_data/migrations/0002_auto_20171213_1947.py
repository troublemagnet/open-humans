# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-12-13 19:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_data', '0001_squashed_0004_auto_20151230_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='enrollment_date',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='signature',
        ),
    ]
