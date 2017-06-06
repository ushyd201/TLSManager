# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='setting',
            name='default_email',
            field=models.EmailField(default=b'security.engineering@rackspace.com', max_length=254),
        ),
    ]
