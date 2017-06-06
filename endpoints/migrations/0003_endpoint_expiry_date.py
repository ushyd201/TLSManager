# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0002_auto_20150930_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='expiry_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
