# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20150611_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headcount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('total_users', models.IntegerField()),
                ('laptop_users', models.IntegerField()),
                ('ss_users', models.IntegerField()),
                ('group_users', models.IntegerField()),
                ('gs_users', models.IntegerField()),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(to='blog.Location')),
            ],
        ),
    ]
