# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='vote',
            new_name='votes',
        ),
        migrations.AlterField(
            model_name='question',
            name='pubdate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'publication_date'),
        ),
    ]
