# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_news_impact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='impact',
        ),
    ]
