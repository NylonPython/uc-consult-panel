# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0006_auto_20150621_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='printrefund',
            name='refund_reason',
            field=models.TextField(default=b'Printing Error', verbose_name=b'Reason for Refund'),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 45, 5, 619767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 45, 5, 620619, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='timesheeterror',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 21, 20, 45, 5, 622675, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 45, 5, 621683, tzinfo=utc)),
        ),
    ]
