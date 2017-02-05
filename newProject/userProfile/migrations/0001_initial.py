# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-31 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCurricularActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityName', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('participationOrAward', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(max_length=6)),
                ('mobile', models.IntegerField(null=True)),
                ('address', models.TextField()),
                ('boardX', models.CharField(max_length=10)),
                ('streamX', models.CharField(max_length=10)),
                ('marksX', models.IntegerField(null=True)),
                ('yearX', models.IntegerField(null=True)),
                ('boardXII', models.CharField(max_length=10)),
                ('streamXII', models.CharField(max_length=10)),
                ('marksXII', models.IntegerField(null=True)),
                ('yearXII', models.IntegerField(null=True)),
                ('college', models.CharField(max_length=10)),
                ('course', models.CharField(max_length=10)),
                ('cgpa', models.IntegerField(null=True)),
                ('gradYear', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='extracurricularactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userProfile.User'),
        ),
    ]
