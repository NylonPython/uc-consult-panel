# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20150621_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='printrefund',
            name='is_refunded',
            field=models.BooleanField(default=False, verbose_name=b'Refunded'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 52, 17, 426721, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 52, 17, 427598, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='timesheeterror',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 21, 20, 52, 17, 429623, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 52, 17, 428685, tzinfo=utc)),
        ),
    ]
