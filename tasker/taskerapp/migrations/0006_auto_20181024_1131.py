# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-10-24 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskerapp', '0005_auto_20181024_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(default='My status', max_length=500),
            preserve_default=False,
        ),
    ]