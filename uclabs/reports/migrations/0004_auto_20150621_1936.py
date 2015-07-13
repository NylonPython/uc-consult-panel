# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20150611_1944'),
        ('reports', '0003_auto_20150621_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheetError',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 6, 21, 19, 36, 17, 971744, tzinfo=utc))),
                ('time_in', models.TimeField()),
                ('time_out', models.TimeField()),
                ('error_reason', models.TextField(max_length=150)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(to='blog.Location')),
            ],
        ),
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 36, 17, 968688, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 36, 17, 969661, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 36, 17, 970807, tzinfo=utc)),
        ),
    ]
