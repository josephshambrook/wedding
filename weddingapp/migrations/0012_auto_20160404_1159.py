# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0011_auto_20160321_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='transport',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invite',
            name='code',
            field=models.CharField(default=b'8696', max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='rsvp_completed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
