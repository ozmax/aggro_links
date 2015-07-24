# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0007_auto_20150724_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='user',
            new_name='owner',
        ),
    ]
