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
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('ann_type', models.IntegerField(default=-1, choices=[(0, b'Neutral'), (-1, b'Negative'), (1, b'Positive')])),
                ('ann_text', models.TextField()),
                ('employee', models.ForeignKey(related_name='employee', to=settings.AUTH_USER_MODEL)),
                ('supervisor', models.ForeignKey(related_name='supervisor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
