# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-06 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0021_auto_20160906_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='actual',
            field=models.CharField(blank=True, choices=[('exact', 'Exact'), ('similar', 'Similar')], default='exact', max_length=2),
        ),
        migrations.AlterField(
            model_name='gift',
            name='category',
            field=models.CharField(blank=True, choices=[('kitchen', 'Kitchen'), ('electric', 'Electric Items'), ('crockery', 'Crockery'), ('glass', 'Glasses'), ('cutlery', 'Cutlery'), ('knives', 'Knives'), ('pots_pans', 'Pots and Pans'), ('linens', 'Linens'), ('house', 'Houseware'), ('other', 'Other')], default='kitchen', max_length=2),
        ),
        migrations.AlterField(
            model_name='gift',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='invite',
            name='code',
            field=models.CharField(default='0731', max_length=6, unique=True),
        ),
    ]
