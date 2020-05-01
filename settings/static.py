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

from . import BASE_DIR

# File upload permissions
# https://docs.djangoproject.com/en/dev/ref/settings/#file-upload-permissions
FILE_UPLOAD_PERMISSIONS = 0o644

_media = 'media'
MEDIA_ROOT = BASE_DIR.joinpath(_media)
MEDIA_URL = f'/{_media}/'

STATICFILES_DIRS = []
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

_static = 'static'
STATIC_ROOT = BASE_DIR.joinpath(_static)
STATIC_URL = f'/{_static}/'
