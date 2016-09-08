# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.serializers.json
import decimal
import postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDRImport',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('switch', models.CharField(max_length=80)),
                ('cdr_source_type', models.IntegerField(null=True, blank=True)),
                ('callid', models.CharField(max_length=80)),
                ('caller_id_number', models.CharField(max_length=80)),
                ('caller_id_name', models.CharField(max_length=80)),
                ('destination_number', models.CharField(max_length=80)),
                ('dialcode', models.CharField(max_length=10, blank=True)),
                ('state', models.CharField(max_length=5, blank=True)),
                ('channel', models.CharField(max_length=80, blank=True)),
                ('starting_date', models.DateTimeField()),
                ('duration', models.IntegerField()),
                ('billsec', models.IntegerField()),
                ('progresssec', models.IntegerField(null=True, blank=True)),
                ('answersec', models.IntegerField(null=True, blank=True)),
                ('waitsec', models.IntegerField(null=True, blank=True)),
                ('hangup_cause_id', models.IntegerField(null=True, blank=True)),
                ('hangup_cause', models.CharField(max_length=80, blank=True)),
                ('direction', models.IntegerField(null=True, blank=True)),
                ('country_code', models.CharField(max_length=3, blank=True)),
                ('accountcode', models.CharField(max_length=40, blank=True)),
                ('buy_rate', models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)),
                ('buy_cost', models.DecimalField(null=True, max_digits=12, decimal_places=5, blank=True)),
                ('sell_rate', models.DecimalField(null=True, max_digits=10, decimal_places=5, blank=True)),
                ('sell_cost', models.DecimalField(null=True, max_digits=12, decimal_places=5, blank=True)),
                ('call_record', models.CharField(max_length=256)),
                ('imported', models.BooleanField(default=False)),
                ('extradata', postgres.fields.JSONField(decode_kwargs={'parse_float': decimal.Decimal}, encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, blank=True)),
            ],
            options={
                'db_table': 'cdr_import',
                'verbose_name': 'CDR Import',
                'verbose_name_plural': 'CDRs Import',
            },
            bases=(models.Model,),
        ),
    ]
