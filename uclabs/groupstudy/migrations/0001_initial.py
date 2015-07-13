# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150611_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupStudyRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_number', models.CharField(max_length=20)),
                ('location', models.ForeignKey(to='blog.Location')),
            ],
        ),
        migrations.CreateModel(
            name='GroupStudyRoomReservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reservation_date', models.DateField()),
                ('reservation_start', models.TimeField()),
                ('reservation_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupStudyRoomSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_study_room', models.ForeignKey(to='groupstudy.GroupStudyRoom')),
            ],
        ),
        migrations.AddField(
            model_name='groupstudyroomreservation',
            name='group_study_room_schedule',
            field=models.ForeignKey(to='groupstudy.GroupStudyRoomSchedule'),
        ),
    ]
