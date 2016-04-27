# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 10:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0012_auto_20160404_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='transport',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invite',
            name='code',
            field=models.CharField(default=b'6468', max_length=6, unique=True),
        ),
    ]
