# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 00:59
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('email_validationApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='email',
            managers=[
                ('emailManager', django.db.models.manager.Manager()),
            ],
        ),
    ]