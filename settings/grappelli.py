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

See for more details: https://github.com/sehmaschine/django-grappelli.

"""

# The Site Title of your admin interface.
GRAPPELLI_ADMIN_TITLE = 'Профстройторг'

# A dictionary containing search patterns for models you cannot (or should not)
# alter.
GRAPPELLI_AUTOCOMPLETE_SEARCH_FIELDS = {
    'auth': {
        'user': ('first_name__icontains', 'last_name__icontains',
                 'username__icontains', 'email__icontains'),
        'group': ('name__icontains', ),
    }
}

GRAPPELLI_INDEX_DASHBOARD = 'dashboard.ProjectDashboard'
