# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modmodels', '0004_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default='erik@erik.com', editable=False, max_length=30),
        ),
    ]