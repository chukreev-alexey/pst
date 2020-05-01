# -*- coding: utf-8 -*-
#
# Copyright 2020 ITCase (info@itcase.pro)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from copy import deepcopy

from django.utils.log import DEFAULT_LOGGING

LOGGING = deepcopy(DEFAULT_LOGGING)

# ****************************************************************
# DJANGO

if 'formatters' not in LOGGING:
    LOGGING['formatters'] = {}

LOGGING['formatters'].update({
    'pretty': {
        'format': '%(levelname)s %(asctime)s %(message)s'
    },
})

if 'handlers' not in LOGGING:
    LOGGING['handlers'] = {}

# Handler for disabled loggers
LOGGING['handlers']['null'] = {'class': 'logging.NullHandler'}

# Allow catch 40x HTTP errors
LOGGING['handlers']['mail_admins']['level'] = 'CRITICAL'

# Disable any supposed filters
try:
    del LOGGING['handlers']['console']['filters']
except KeyError:
    pass

LOGGING['handlers']['console']['formatter'] = 'pretty'

if 'loggers' not in LOGGING:
    LOGGING['loggers'] = {}

# Disable 'Invalid HTTP_HOST' errors
LOGGING['loggers']['django.security.DisallowedHost'] = {
    'handlers': ['null'],
    'propagate': False,
}

# ****************************************************************
# PROJECT

_format = LOGGING['formatters']['pretty']['format']

# Uses for custom management commands
LOGGING['formatters']['management'] = {'format': 'MANAGEMENT ' + _format}
LOGGING['handlers']['management'] = {
    'class': 'logging.StreamHandler',
    'formatter': 'management',
    'level': 'DEBUG',
}
LOGGING['loggers']['management'] = {
    'handlers': ['management'],
    'level': 'WARNING',
}

# ****************************************************************
# THIRD-PARTY

# Django RQ
# https://github.com/rq/django-rq
LOGGING['formatters']['rq_console'] = {'format': '%(asctime)s %(message)s'}
LOGGING['handlers']['rq_console'] = {
    'level': 'DEBUG',
    'class': 'rq.utils.ColorizingStreamHandler',
    'formatter': 'rq_console',
    'exclude': ['%(asctime)s'],
}
LOGGING['loggers']['rq.worker'] = {
    'handlers': ('rq_console', 'sentry'),
    'level': 'WARNING'
}

# Sentry
# https://github.com/getsentry/sentry
LOGGING['root'] = {'level': 'WARNING', 'handlers': ['sentry']}
LOGGING['handlers']['sentry'] = {
    'level': 'WARNING',
    'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
    'filters': ['require_debug_false'],
}
