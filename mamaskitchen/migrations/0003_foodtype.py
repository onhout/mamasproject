# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mamaskitchen', '0002_menupicurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('menuitems', models.ManyToManyField(to='mamaskitchen.MenuItem')),
            ],
        ),
    ]