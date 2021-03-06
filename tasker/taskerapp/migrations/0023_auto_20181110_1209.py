# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-10 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskerapp', '0022_auto_20181104_0616'),
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
            field=models.ImageField(blank=True, null=True, upload_to='task_logo/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
