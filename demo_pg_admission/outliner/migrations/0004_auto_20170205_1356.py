# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-05 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outliner', '0003_auto_20170205_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]