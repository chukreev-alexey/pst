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

"""Custom dashboard for Django Grappelli.

See for more details:
https://django-grappelli.readthedocs.io/en/latest/dashboard_setup.html
"""

from django.urls import reverse_lazy

from grappelli.dashboard import modules, Dashboard


class ProjectDashboard(Dashboard):

    def init_with_context(self, context):

        request = context['request']

        self.children.append(modules.AppList(
            title='Управление сайтом',
            collapsible=True,
            css_classes=('grp-closed', ),
            column=1,
            models=('django.contrib.*', )
        ))
        self.children.append(modules.AppList(
            title='Приложения',
            collapsible=True,
            column=1,
            exclude=('django.contrib.*', )
        ))

        if request.user.is_superuser:
            self.children.append(self.get_site_part())

        self.children.append(modules.LinkList(
            title='Управление файлами',
            collapsible=False,
            column=2,
            children=(
                {
                    'title': 'Менеджер файлов',
                    'url': reverse_lazy('filebrowser:fb_browse',
                                        current_app='filebrowser'),
                },
            )
        ))

        self.children.append(modules.RecentActions(
            'Последние действия',
            limit=5,
            collapsible=False,
            column=2,
        ))

    def get_site_part(self):
        children = [{'title': 'Django RQ', 'url': reverse_lazy('rq_home')}]
        return modules.LinkList(title='Cайт', collapsible=False, column=2,
                                children=children)
