# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coursesApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='desctiption',
            new_name='description',
        ),
    ]