# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('computer_speed', models.IntegerField()),
                ('computer_memory', models.IntegerField()),
                ('computer_comment', models.CharField(max_length=250, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=100)),
                ('model_num', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lab_type', models.IntegerField(default=0, choices=[(1, b'Classroom Labs'), (-1, b'Affiliate Labs'), (0, b'Open Labs')])),
                ('name', models.CharField(max_length=100)),
                ('building', models.CharField(max_length=100)),
                ('open_time', models.DateTimeField(verbose_name=b'Open Time')),
                ('close_time', models.DateTimeField(verbose_name=b'Close Time')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('post_content', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('printer_comment', models.CharField(max_length=250, blank=True)),
                ('printer_location', models.ForeignKey(to='blog.Location')),
                ('printer_model', models.ForeignKey(to='blog.HardwareModel')),
            ],
        ),
        migrations.AddField(
            model_name='computer',
            name='computer_location',
            field=models.ForeignKey(to='blog.Location'),
        ),
        migrations.AddField(
            model_name='computer',
            name='computer_model',
            field=models.ForeignKey(to='blog.HardwareModel'),
        ),
    ]
