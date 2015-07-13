# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='computer',
            field=models.ForeignKey(default=1, to='blog.Computer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='computer_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='printer',
            field=models.ForeignKey(default=1, to='blog.Printer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='printer_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='computer',
            name='computer_location',
            field=models.ForeignKey(related_name='lab_computer', to='blog.Location'),
        ),
        migrations.AlterField(
            model_name='printer',
            name='printer_location',
            field=models.ForeignKey(related_name='lab_printer', to='blog.Location'),
        ),
    ]
