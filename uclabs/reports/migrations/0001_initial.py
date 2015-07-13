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
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 1, 29, 298220, tzinfo=utc))),
                ('ann_type', models.IntegerField(default=-1, verbose_name=b'Annotation Type', choices=[(0, b'Neutral'), (-1, b'Negative'), (1, b'Positive')])),
                ('ann_text', models.TextField(verbose_name=b'Annotation')),
                ('employee', models.ForeignKey(related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(related_name='supervisor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Headcount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 6, 21, 19, 1, 29, 299130, tzinfo=utc))),
                ('total_users', models.IntegerField(verbose_name=b'Total Users')),
                ('laptop_users', models.IntegerField(verbose_name=b'Laptop Users')),
                ('ss_users', models.IntegerField(verbose_name=b'Silent Study Ussers')),
                ('group_users', models.IntegerField(verbose_name=b'Users in Groups')),
                ('gs_users', models.IntegerField(verbose_name=b'Users in Group Study Room')),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(to='blog.Location')),
            ],
            options={
                'permissions': (('can_view_headcounts', 'Can View Headcount'),),
            },
        ),
    ]
