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
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TroubleTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 19, 21, 444329, tzinfo=utc))),
                ('machine_name', models.CharField(max_length=50)),
                ('issue_description', models.TextField(max_length=500)),
                ('is_solved', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(to='blog.Location')),
            ],
        ),
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 19, 21, 442451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 19, 21, 443298, tzinfo=utc)),
        ),
    ]
