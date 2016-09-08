# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_cdr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdrimport',
            name='custom_billsec',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cdrimport',
            name='custom_destination_number',
            field=models.CharField(max_length=80, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cdrimport',
            name='custom_filds',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
