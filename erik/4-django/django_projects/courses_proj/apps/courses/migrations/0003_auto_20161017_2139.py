# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20161017_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='id',
        ),
        migrations.AddField(
            model_name='description',
            name='course',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courses.Course'),
        ),
    ]