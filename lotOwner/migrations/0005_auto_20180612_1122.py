# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lotOwner', '0004_auto_20180612_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='onwer',
            new_name='owner',
        ),
    ]
