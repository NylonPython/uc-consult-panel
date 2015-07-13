# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0007_auto_20150621_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 45, 10, 87971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 45, 10, 88867, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='timesheeterror',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 21, 20, 45, 10, 90932, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 45, 10, 89935, tzinfo=utc)),
        ),
    ]
