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

ALLOWED_HOSTS = ['*.pst.example.com']
DEBUG = False

# DATABASES
from .core import DATABASES  # noqa
DATABASES['default']['PASSWORD'] =

# EMAIL
# put here only password, other settings in `core.py`
EMAIL_HOST_PASSWORD =

# ****************************************************************
# THIRD-PARTY

# Sentry
# See for more details: https://docs.sentry.io/
RAVEN_CONFIG = {'dsn': }

