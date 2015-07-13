# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20150621_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headcount',
            options={},
        ),
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 50, 20, 579173, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 50, 20, 580030, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='timesheeterror',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 21, 19, 50, 20, 582060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 50, 20, 581099, tzinfo=utc)),
        ),
    ]
