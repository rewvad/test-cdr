.. _configuration-freeswitch:

Configuration for FreeSWITCH
============================

Import configuration for FreeSWITCH
-----------------------------------

Review your database settings and ensure the second database exists and that is configured correctly::

    # DATABASE SETTINGS
    # =================
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'cdrstats-billing',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5433',
            'OPTIONS': {
                # Postgresql Autocommit
                'autocommit': True,
            }
        },
        'import_cdr': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'cdr-pusher',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5433',
            'OPTIONS': {
                'autocommit': True,
            }
        }
    }

You will need to push your CDRs from FreeSWITCH CDR datastore to a CDR-Stats 'import_cdr' database.
To help on this job we created CDR-Pusher, please visit the website and the instructions there to install and configure CDR-Stats correctly: https://github.com/cdr-stats/cdr-stats


.. _realtime-configuration-freeswitch:

Realtime configuration for FreeSWITCH
=====================================

The FreeSWITCH Event Socket Library allow CDR-Stats to retrieve Realtime information to show the number of concurrent calls both in realtime and historically.

The collection of realtime information is done via Collectd (https://collectd.org/) and InfluxDB (http://influxdb.com/.

CDR-Stats can get CDR from both Freeswitch and Asterisk, or a combination of both. Other Telco Switches are supported, please contact us for further information.
