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

# ****************************************************************
# DJANGO


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['.pst.itcase.pro']

# DATABASES
from .core import DATABASES  # noqa
DATABASES['default']['PASSWORD'] =

# EMAIL
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD =
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_PORT = 465
EMAIL_USE_TLS = True

# LOGGING
from .logging import LOGGING  # noqa
LOGGING['loggers']['management']['level'] = 'ERROR'

# ****************************************************************
# THIRD-PARTY

# Sentry
# See for more details: https://docs.sentry.io/
import sentry_sdk  # noqa
from sentry_sdk.integrations.django import DjangoIntegration  # noqa
from sentry_sdk.integrations.rq import RqIntegration  # noqa
sentry_sdk.init(
    dsn=,
    integrations=[DjangoIntegration(), RqIntegration()],
    send_default_pii=True
)
