# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20160406_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female'), (b'D', b'Data Not Available')], default='D', max_length=1),
        ),
    ]