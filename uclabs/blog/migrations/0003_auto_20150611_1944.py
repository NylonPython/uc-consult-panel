# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150610_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='printer',
        ),
        migrations.AlterField(
            model_name='printer',
            name='printer_location',
            field=models.ForeignKey(related_name='lab_printers', to='blog.Location'),
        ),
    ]
