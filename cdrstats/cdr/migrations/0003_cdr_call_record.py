# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdr', '0002_remove_cdr_call_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='call_record',
            field=models.CharField(max_length=256, null=True, verbose_name='call record', blank=True),
            preserve_default=True,
        ),
    ]
