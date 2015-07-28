# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0012_auto_20150728_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='group_name',
            new_name='name',
        ),
    ]
