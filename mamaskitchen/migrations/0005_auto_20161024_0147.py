# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mamaskitchen', '0004_auto_20161024_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItemRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamaskitchen.MenuItem')),
            ],
        ),
        migrations.RemoveField(
            model_name='foodtype',
            name='itemstype',
        ),
        migrations.AddField(
            model_name='foodtype',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 10, 24, 1, 47, 4, 660694, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='foodtype',
            name='type',
        ),
        migrations.AddField(
            model_name='fooditemrelationship',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamaskitchen.FoodType'),
        ),
        migrations.AddField(
            model_name='foodtype',
            name='type',
            field=models.ManyToManyField(through='mamaskitchen.FoodItemRelationship', to='mamaskitchen.MenuItem'),
        ),
    ]
