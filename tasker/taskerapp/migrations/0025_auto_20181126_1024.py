# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-26 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskerapp', '0024_auto_20181123_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='category',
            field=models.CharField(choices=[('ЕГЭ егэ английский Английский Язык язык', 'ЕГЭ:Английский язык'), ('IELTS ielts шудеы', 'IELTS'), ('TOEFL toefl ещуад', 'TOEFL')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='logo',
            field=models.ImageField(blank=True, upload_to='task_logo/'),
        ),
    ]
