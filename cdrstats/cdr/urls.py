#
# CDR-Stats License
# http://www.cdr-stats.org
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2015 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.conf.urls import patterns


urlpatterns = patterns('cdr.views',
                       (r'^cdr_view/$', 'cdr_view'),
                       (r'^cdr_view/callrecord/(?P<filename>.*)/$', 'cdr_callrecord'),
                       (r'^cdr_export_csv/$', 'cdr_export_to_csv'),
                       (r'^cdr_detail/(?P<cdr_id>\w+)/$', 'cdr_detail'),
                       (r'^dashboard/$', 'cdr_dashboard'),
                       (r'^daily_comparison/$', 'cdr_daily_comparison'),
                       (r'^overview/$', 'cdr_overview'),
                       (r'^mail_report/$', 'mail_report'),
                       (r'^country_report/$', 'cdr_country_report'),
                       (r'^world_map/$', 'world_map_view'),
                       )
