# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-06 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0019_auto_20160905_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='actual',
            field=models.CharField(blank=True, choices=[('exact', 'Exact'), ('similar', 'Similar')], default='exact', max_length=200),
        ),
        migrations.AddField(
            model_name='gift',
            name='category',
            field=models.CharField(choices=[('kitchen', 'Kitchen'), ('electric', 'Electric Items'), ('crockery', 'Crockery'), ('glass', 'Glasses'), ('cutlery', 'Cutlery'), ('knives', 'Knives'), ('pots_pans', 'Pots and Pans'), ('linens', 'Linens'), ('house', 'Houseware'), ('other', 'Other')], default='kitchen', max_length=200),
        ),
        migrations.AlterField(
            model_name='gift',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='code',
            field=models.CharField(default='0866', max_length=6, unique=True),
        ),
    ]
