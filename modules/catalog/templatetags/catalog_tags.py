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

from decimal import Decimal

from django import template

from ..models import Category

register = template.Library()


@register.inclusion_tag('itcase_catalog/include/catalog_group_hidden.html')
def catalog_group_hidden(category=None, limit=5):
    if not category:
        return {}

    subcategories = category.get_children_active()
    hidden_categories_count = subcategories.count() - limit
    if hidden_categories_count <= 0:
        hidden_categories_count = 0

    return {
        'subcategories': subcategories,
        'limit': str(limit),
        'hidden_categories_count': hidden_categories_count
    }


@register.inclusion_tag('itcase_catalog/include/catalog_menu.html',
                        takes_context=True)
def catalog_menu(context,
                 queryset=None,
                 additional_class=None,
                 title_additional_class=None):
    queryset = queryset or Category.objects.filter(active=True, in_menu=True)
    if queryset:
        context['menu_queryset'] = queryset

    if additional_class is None:
        additional_class = context.get('additional_class')

    if additional_class is not None:
        context['additional_class'] = str(additional_class)

    if title_additional_class is not None:
        context['title_additional_class'] = str(title_additional_class)

    return context


@register.inclusion_tag('itcase_catalog/include/catalog_menu_footer.html',
                        takes_context=True)
def catalog_menu_footer(context, queryset=None):
    queryset = queryset or Category.objects.filter(active=True, level=0)
    if queryset:
        context['menu_queryset'] = queryset
    return context


@register.inclusion_tag('itcase_catalog/include/get_categories_by_level.html',
                        takes_context=True)
def get_categories_by_level(context, level):
    context['categories_list'] = Category.objects.filter(active=True,
                                                         level=level)
    return context


@register.filter
def get_product_actual_price(product, price_query):
    try:
        _max = Decimal(price_query['max'])
        _min = Decimal(price_query['min'])
    except (KeyError, TypeError, ValueError):
        _max = _min = None

    result = None
    for price in product.prices.all():
        _price = price.price
        if _max is not None and _min is not None:
            if _price > _max or _price < _min:
                continue

        if not result:
            result = price

        if _price < result.price:
            result = price

    return result
