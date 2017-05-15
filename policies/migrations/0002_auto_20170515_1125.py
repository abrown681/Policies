# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rule',
            old_name='us_gov',
            new_name='US_Government',
        ),
        migrations.RemoveField(
            model_name='rule',
            name='priority_level',
        ),
        migrations.AddField(
            model_name='rule',
            name='priority',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Priority level'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='citizenship',
            field=models.CharField(choices=[('USA', 'United States'), ('GBR', 'Great Britian'), ('CAN', 'Canada'), ('AUS', 'Australia'), ('NZL', 'New Zealand')], max_length=3),
        ),
        migrations.AlterField(
            model_name='rule',
            name='clear_level',
            field=models.CharField(choices=[('UC', 'UNCLASSIFIED'), ('CF', 'CONFIDENTIAL'), ('S', 'SECRET'), ('TS', 'TOP_SECRET')], max_length=2, verbose_name='Clearance level'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='rule',
            name='day',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Day requirement'),
        ),
        migrations.AlterField(
            model_name='rule',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Policy name'),
        ),
    ]
