# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20150611_1944'),
        ('reports', '0005_auto_20150621_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrintRefund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_m_number', models.CharField(max_length=9, verbose_name=b'M-Number (include M)')),
                ('num_pages', models.IntegerField()),
                ('print_type', models.IntegerField(default=0, verbose_name=b'Type of Prints', choices=[(0, b'Black and White'), (1, b'Color')])),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(to='blog.Location')),
                ('printer', models.ForeignKey(to='blog.Printer')),
            ],
        ),
        migrations.AlterModelOptions(
            name='headcount',
            options={'permissions': (('can_view_headcounts', 'Can View Headcount'),)},
        ),
        migrations.AlterField(
            model_name='annotation',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 41, 21, 353042, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='headcount',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 41, 21, 353902, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='timesheeterror',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 6, 21, 20, 41, 21, 355935, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 21, 20, 41, 21, 354996, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='is_solved',
            field=models.BooleanField(default=False, verbose_name=b'Resolved'),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='issue_description',
            field=models.TextField(max_length=500, verbose_name=b'Description'),
        ),
        migrations.AlterField(
            model_name='troubleticket',
            name='machine_name',
            field=models.CharField(max_length=50, verbose_name=b'Machine Name'),
        ),
    ]
