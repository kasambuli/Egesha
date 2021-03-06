# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('lotOwner', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.TimeField(auto_now_add=True)),
                ('time_out', models.TimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.DriverProfile')),
                ('lotdetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotOwner.LotDetails')),
            ],
        ),
        migrations.CreateModel(
            name='Cardetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_plate', models.CharField(default='KCA101Z', max_length=30, null=True)),
                ('car_make', models.CharField(default='RangeRover', max_length=30, null=True)),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.DriverProfile')),
            ],
        ),
    ]
