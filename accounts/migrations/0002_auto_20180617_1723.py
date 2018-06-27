# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-17 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='managerprofile',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='ownerprofile',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=30, null=True),
        ),
    ]
