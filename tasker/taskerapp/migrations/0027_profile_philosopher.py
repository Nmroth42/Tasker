# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-07 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskerapp', '0026_auto_20181126_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='philosopher',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
