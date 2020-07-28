# -*- coding: utf-8 -*-
#
# Copyright 2017 ItCase (info@itcase.pro)
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

from django import template

register = template.Library()

__all__ = ['catalog_menu']


@register.inclusion_tag('itcase_catalog/include/catalog_nav.html',
                        takes_context=True)
def catalog_menu(context, additional_class=None, title_additional_class=None,
                 queryset=None):
    from ..models import Category

    queryset = queryset or Category.objects.filter(level=0)
    context['catalog_menu'] = queryset

    if additional_class is None:
        additional_class = context.get('additional_class')

    if additional_class is not None:
        context['additional_class'] = str(additional_class)

    if title_additional_class is not None:
        context['title_additional_class'] = str(title_additional_class)

    return context


@register.inclusion_tag('itcase_catalog/include/subcategories_list.html',
                        takes_context=True)
def first_level_subcategories(context):
    from ..models import Category
    context['first_level_subcategories'] = Category.objects.filter(level=1)
    return context
