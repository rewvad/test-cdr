# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cdr', '0003_cdr_call_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='custom_carrier',
            field=models.CharField(max_length=80, null=True, verbose_name='carrier', blank=True),
            preserve_default=True,
        ),
    ]
