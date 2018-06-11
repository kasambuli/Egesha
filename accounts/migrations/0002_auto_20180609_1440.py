# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driverprofile',
            name='license',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AddField(
            model_name='managerprofile',
            name='national_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='ownerprofile',
            name='national_id',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='managerprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ownerprofile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]