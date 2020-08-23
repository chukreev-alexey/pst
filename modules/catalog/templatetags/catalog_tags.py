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

from django import template

from ..models import Category

register = template.Library()

__all__ = ['catalog_menu']


@register.inclusion_tag('itcase_catalog/include/catalog_menu.html',
                        takes_context=True)
def catalog_menu(context, additional_class=None, title_additional_class=None,
                 queryset=None):
    '''
        catalog_menu поставляется из
        catalog.context_processors.base_categories
    '''
    if queryset is not None:
        context['catalog_menu'] = queryset

    if additional_class is None:
        additional_class = context.get('additional_class')

    if additional_class is not None:
        context['additional_class'] = str(additional_class)

    if title_additional_class is not None:
        context['title_additional_class'] = str(title_additional_class)

    return context


@register.inclusion_tag('itcase_catalog/include/catalog_footer_menu.html',
                        takes_context=True)
def footer_categories_tag(context, queryset=None):
    '''
        footer_categories поставляется из
        catalog.context_processors.base_categories
    '''
    if queryset is not None:
        context['footer_categories'] = queryset
    return context


@register.inclusion_tag('itcase_catalog/include/get_categories_by.html',
                        takes_context=True)
def get_categories_by(context, queryset=None, **kwargs):
    categories = ()
    if queryset is not None:
        categories = queryset
    elif 'level' in kwargs:
        categories = Category.objects.filter(level=kwargs['level'])
    context['categories_list'] = categories
    return context


@register.inclusion_tag('itcase_catalog/include/catalog_group_hidden.html')
def catalog_group_hidden(category=None, limit=5):
    if category:
        subcategories = category.children.all()
        count = subcategories.count()
        hidden_categories_count = count - limit
        if hidden_categories_count <= 0:
            hidden_categories_count = 0
        return {'subcategories': subcategories,
                'limit': str(limit),
                'hidden_categories_count': hidden_categories_count}
