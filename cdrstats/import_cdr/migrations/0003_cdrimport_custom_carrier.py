# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_cdr', '0002_auto_20160725_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdrimport',
            name='custom_carrier',
            field=models.CharField(max_length=80, null=True),
            preserve_default=True,
        ),
    ]
