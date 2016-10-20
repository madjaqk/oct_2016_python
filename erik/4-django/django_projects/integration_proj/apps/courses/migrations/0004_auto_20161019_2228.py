# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20161017_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='course',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='description', serialize=False, to='courses.Course'),
        ),
    ]
