# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-24 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mamaskitchen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPicURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('itemurl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mamaskitchen.MenuItem')),
            ],
        ),
    ]