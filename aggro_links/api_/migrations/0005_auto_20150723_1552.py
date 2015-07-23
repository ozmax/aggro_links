# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_', '0004_link_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='entry_date',
            field=models.DateTimeField(),
        ),
    ]
