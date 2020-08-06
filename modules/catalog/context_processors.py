# -*- coding: utf-8 -*-
#
# Copyright 2020 ItCase (info@itcase.pro)
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


from django.urls import reverse


from itcase_catalog.shortcuts import get_category_model


Category = get_category_model()


def base_categories(request):
    '''
        Возвращает QuerySet с категориями, которые будут отображаться
        на всех страницах сайта
    '''

    if not request.path.startswith(reverse('admin:index')):
        return {'catalog_menu': Category.objects.filter(in_menu=True),
                'footer_categories': Category.objects.filter(level=0)}
    return {}