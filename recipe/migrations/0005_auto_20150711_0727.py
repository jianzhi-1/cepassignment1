# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20150711_0720'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='place',
            new_name='region',
        ),
    ]
