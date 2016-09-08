# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.serializers.json
import postgres.fields
import caching.base
import decimal


class Migration(migrations.Migration):

    dependencies = [
        ('country_dialcode', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('switch', '0002_auto_20150929_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDR',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cdr_source_type', models.IntegerField(default=3, null=True, blank=True, choices=[(2, 'API'), (4, 'ASTERISK'), (1, 'CSV UPLOAD'), (3, 'FREESWITCH'), (6, 'KAMAILIO'), (7, 'OPENSIPS'), (8, 'SIPWISE'), (0, 'UNKNOWN'), (9, 'VERAZ'), (5, 'YATE')])),
                ('callid', models.CharField(help_text='VoIP call-ID', max_length=80)),
                ('caller_id_number', models.CharField(max_length=80, verbose_name='CallerID Number', blank=True)),
                ('caller_id_name', models.CharField(max_length=80, verbose_name='CallerID Name', blank=True)),
                ('destination_number', models.CharField(help_text='the international number of the recipient, without the leading +', max_length=80, verbose_name='destination number', db_index=True)),
                ('state', models.CharField(max_length=5, null=True, verbose_name='State/Region', blank=True)),
                ('channel', models.CharField(max_length=80, null=True, verbose_name='channel', blank=True)),
                ('starting_date', models.DateTimeField(verbose_name='starting date', db_index=True)),
                ('duration', models.IntegerField(default=0, verbose_name='duration')),
                ('billsec', models.IntegerField(default=0, verbose_name='bill sec')),
                ('progresssec', models.IntegerField(default=0, null=True, verbose_name='progress sec', blank=True)),
                ('answersec', models.IntegerField(default=0, null=True, verbose_name='answer sec', blank=True)),
                ('waitsec', models.IntegerField(default=0, null=True, verbose_name='wait sec', blank=True)),
                ('direction', models.IntegerField(default=1, db_index=True, verbose_name='direction', choices=[(1, 'INBOUND'), (0, 'NOT DEFINED'), (2, 'OUTBOUND')])),
                ('authorized', models.BooleanField(default=False, verbose_name='authorized')),
                ('call_type', models.IntegerField(default=0, null=True, blank=True, choices=[(2, 'INTERNAL'), (0, 'INTERNATIONAL'), (1, 'INTERNATIONAL')])),
                ('accountcode', models.CharField(max_length=80, verbose_name='account code', blank=True)),
                ('buy_rate', models.DecimalField(default=0, verbose_name='Buy Rate', max_digits=10, decimal_places=5)),
                ('buy_cost', models.DecimalField(default=0, verbose_name='Buy Cost', max_digits=12, decimal_places=5)),
                ('sell_rate', models.DecimalField(default=0, verbose_name='Sell Rate', max_digits=10, decimal_places=5)),
                ('sell_cost', models.DecimalField(default=0, verbose_name='Sell Cost', max_digits=12, decimal_places=5)),
                ('call_record', models.CharField(max_length=256, null=True, verbose_name='call record', blank=True)),
                ('data', postgres.fields.JSONField(encode_kwargs={'cls': django.core.serializers.json.DjangoJSONEncoder}, decode_kwargs={'parse_float': decimal.Decimal})),
                ('country', models.ForeignKey(verbose_name='country', blank=True, to='country_dialcode.Country', null=True)),
                ('dialcode', models.ForeignKey(verbose_name='dialcode', blank=True, to='country_dialcode.Prefix', null=True)),
            ],
            options={
                'db_table': 'voip_cdr',
                'verbose_name': 'Call',
                'verbose_name_plural': 'Calls',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HangupCause',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.PositiveIntegerField(help_text='ITU-T Q.850 Code', unique=True, verbose_name='code')),
                ('enumeration', models.CharField(max_length=100, null=True, verbose_name='enumeration', blank=True)),
                ('cause', models.CharField(max_length=100, null=True, verbose_name='cause', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
            ],
            options={
                'db_table': 'hangup_cause',
                'verbose_name': 'hangup cause',
                'verbose_name_plural': 'hangup causes',
            },
            bases=(caching.base.CachingMixin, models.Model),
        ),
        migrations.AddField(
            model_name='cdr',
            name='hangup_cause',
            field=models.ForeignKey(verbose_name='hangup cause', to='cdr.HangupCause'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cdr',
            name='switch',
            field=models.ForeignKey(verbose_name='Switch', to='switch.Switch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cdr',
            name='user',
            field=models.ForeignKey(related_name='Call Owner', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
