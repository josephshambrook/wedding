# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0015_auto_20160422_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='song_requests',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='code',
            field=models.CharField(default=b'3108', max_length=6, unique=True),
        ),
    ]
