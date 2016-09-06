# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-06 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weddingapp', '0022_auto_20160906_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='category',
            field=models.CharField(choices=[('kitchen', 'Kitchen'), ('electric', 'Electric Items'), ('crockery', 'Crockery'), ('glass', 'Glasses'), ('cutlery', 'Cutlery'), ('knives', 'Knives'), ('pots_pans', 'Pots and Pans'), ('linens', 'Linens'), ('house', 'Houseware'), ('other', 'Other')], default='kitchen', max_length=2),
        ),
        migrations.AlterField(
            model_name='invite',
            name='code',
            field=models.CharField(default='3860', max_length=6, unique=True),
        ),
    ]
