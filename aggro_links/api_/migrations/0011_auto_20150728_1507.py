# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0010_auto_20150728_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='group',
        ),
        migrations.AddField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(to='api_.Group', null=True, blank=True),
        ),
    ]
