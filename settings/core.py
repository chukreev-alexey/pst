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

"""Main settings for project."""

from . import BASE_DIR
from .project import PROJECT_NAME

# A list of all the people who get code error notifications
ADMINS = [('ITCase', 'error@itcase.pro')]
# A list in the same format as ADMINS that specifies who should get broken link
# notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# This is used to provide cryptographic signing, and should be set to a unique,
# unpredictable value.
SECRET_KEY = '9+1ujg9p4-xph4g0yvn1putkb^#j+q)-c!lp)1g&d!v2@%wzd#'

# A list of strings designating all applications that are enabled.
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'captcha',
    'compressor',
    'django_mptt_admin',
    'django_rq',
    'tinymce_4',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'mptt',
    'raven.contrib.django.raven_compat',
    'rest_framework',
    'rest_framework.authtoken',

    'itcase_cart',
    'itcase_catalog',
    'itcase_common',
    'itcase_entry',
    'itcase_feed',
    'itcase_gallery',
    'itcase_logos',
    'itcase_pages',
    'itcase_paginator',
    'itcase_rotator',
    'itcase_search',

    'modules.catalog',

    'website',

    'forms_builder.forms',

    'django.contrib.admin',
]

# A list of middleware to use
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'itcase_pages.middleware.PageMiddleware',
]

# A string representing the full Python import path to your root URLconf.
ROOT_URLCONF = 'urls'

# A list containing the settings for all template engines.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'itcase_common.context_processors.common',
                'itcase_pages.context_processors.page',

                'modules.catalog.context_processors.base_categories',
            ],
        },
    },
]


# A dictionary containing the settings for all databases to be used.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '127.0.0.1',
        'NAME': PROJECT_NAME,
        'PORT': 5432,
        'USER': PROJECT_NAME,
    }
}

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.password_validation'
                 '.NumericPasswordValidator'),
    },
]

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
# A string representing the language code for this installation.
LANGUAGE_CODE = 'ru-ru'
# A boolean that specifies if datetimes will be timezone-aware by default.
USE_TZ = True
TIME_ZONE = 'Asia/Yekaterinburg'
# A boolean that specifies whether Django’s translation system will be enabled.
USE_I18N = True
# A boolean that specifies if localized formatting of data will be enabled.
USE_L10N = True
THOUSAND_SEPARATOR = ' '
USE_THOUSAND_SEPARATOR = True

# Controls where Django stores session data.
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# If you’re using cache-based session storage, this selects the cache to use.
SESSION_CACHE_ALIAS = 'session'

# The ID, as an integer, of the current site in the django_site database table.
SITE_ID = 1

# Settings for sending email
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
EMAIL_HOST = 'localhost'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_PORT = 465
EMAIL_USE_TLS = True
