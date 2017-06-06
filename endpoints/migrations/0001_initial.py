# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('contacts', models.ManyToManyField(to='endpoints.Contact')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default_email', models.EmailField(default=b'security.engineering@rackspace.com', max_length=75)),
                ('scan_enabled', models.BooleanField(default=False)),
                ('default_scan_frequency', models.IntegerField(default=1)),
                ('scan_score_threshold', models.CharField(max_length=16)),
                ('auto_purge', models.BooleanField(default=False)),
                ('test_retention_period', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('ip_address', models.CharField(max_length=256)),
                ('score', models.CharField(max_length=16)),
                ('defects', models.ManyToManyField(to='endpoints.Defect')),
                ('the_endpoint', models.ForeignKey(to='endpoints.Endpoint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='product',
            field=models.ForeignKey(to='endpoints.Product'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endpoint',
            name='test_results',
            field=models.ManyToManyField(to='endpoints.TestResult'),
            preserve_default=True,
        ),
    ]
