# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0008_auto_20150724_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='categories',
            field=models.ManyToManyField(to='api_.Category'),
        ),
    ]
