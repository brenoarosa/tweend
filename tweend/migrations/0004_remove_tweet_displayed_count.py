# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-17 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweend', '0003_auto_20170117_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='displayed_count',
        ),
    ]
