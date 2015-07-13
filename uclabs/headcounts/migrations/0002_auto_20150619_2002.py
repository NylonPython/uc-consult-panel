# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('headcounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headcount',
            options={'permissions': (('can_view_headcounts', 'Can View Headcount'),)},
        ),
    ]
