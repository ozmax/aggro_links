# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0011_auto_20150728_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(to='api_.Group', blank=True),
        ),
    ]
