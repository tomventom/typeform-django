# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 18:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='city_hq',
            new_name='city_headquarters',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='phone_num',
            new_name='phone_number',
        ),
    ]