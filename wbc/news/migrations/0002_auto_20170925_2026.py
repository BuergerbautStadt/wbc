# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='n',
            field=models.IntegerField(verbose_name='Anzahl Mails'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='send',
            field=models.DateTimeField(verbose_name='Gesendet'),
        ),
    ]
