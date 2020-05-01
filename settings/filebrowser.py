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
"""Configure Django FileBrowser.

See for more details: https://github.com/sehmaschine/django-filebrowser.

"""

# Main directory
FILEBROWSER_DIRECTORY = 'uploads/'

# Allowed extensions for file upload
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.gif', '.ico', '.jpg', '.jpeg', '.png', '.tif', '.tiff'],
    'Video': ['.avi', '.mov', '.mpeg', '.mpg', '.rm', '.wmv'],
    'Document': [
        '.csv', '.doc', '.doc', '.docx', '.ods', '.odt', '.pdf', '.ppt',
        '.pptx', '.rtf', '.txt', '.xls'
    ],
    'Embed': ['.swf'],
    'Audio': ['.aiff', '.m4p', '.midi', '.mp3', '.mp4', '.wav'],
    'Code': ['.css', '.html', '.js', '.py']
}

# Max upload size in bytes
FILEBROWSER_MAX_UPLOAD_SIZE = 10485760

# Each key contains an options dict with params that will be forwarded to the
# image processors chain.
FILEBROWSER_VERSIONS = {
    'admin_thumbnail': {
        'verbose_name': 'Admin Thumbnail',
        'width': 60,
        'height': 60,
        'opts': 'crop'
    },
    'big': {
        'verbose_name': 'Big (6 col)',
        'width': 460,
        'height': '',
        'opts': ''
    },
    'large': {
        'verbose_name': 'Large (8 col)',
        'width': 680,
        'height': '',
        'opts': ''
    },
    'medium': {
        'verbose_name': 'Medium (4col )',
        'width': 300,
        'height': '',
        'opts': ''
    },
    'small': {
        'verbose_name': 'Small (2 col)',
        'width': 140,
        'height': '',
        'opts': ''
    },
    'thumbnail': {
        'verbose_name': 'Thumbnail (1 col)',
        'width': 60,
        'height': 60,
        'opts': 'crop'
    },
}

# Directory to save image versions (and thumbnails)
FILEBROWSER_VERSIONS_BASEDIR = '_versions'

# The version being used as the admin thumbnail
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'

# The versions you want to show with the admin interface
FILEBROWSER_ADMIN_VERSIONS = ['thumbnail', 'small', 'medium', 'big', 'large']

# Set different Options for selecting elements from the FileBrowser
FILEBROWSER_SELECT_FORMATS = {
    'folder': ['Folder'],
    'file': ['Audio', 'Document', 'Folder', 'Image', 'Video'],
    'image': ['Image'],
    'document': ['Document', 'Embed'],
    'media': ['Audio', 'Embed', 'Video'],
}
