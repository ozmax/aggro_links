# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0005_auto_20150723_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='text',
        ),
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(default='http://ozmaxplanet.com', max_length=500),
            preserve_default=False,
        ),
    ]
