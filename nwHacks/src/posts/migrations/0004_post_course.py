# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160226_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='course',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]