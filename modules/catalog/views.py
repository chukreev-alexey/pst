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

from itertools import permutations

from django.db.models import Max, Min, Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import ListView

from itcase_catalog.conf import get_template_name
from itcase_catalog.views import ProductDetail as ProductDetailBase
from itcase_common.mixins import FilterMixin, SortMixin
from itcase_common.views.mixins import RequestDataMixin
from itcase_paginator.pagination import SlicePaginatorMixin

from .models import Category, Product, Parametr, Price
from .conf import get_settings


__all__ = ('CatalogIndexView', 'CategoryDetail', 'ProductDetail')


class CatalogIndexView(TemplateView):
    template_name = get_template_name('catalog.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        groups = {
            'recommended': Product.objects.filter(in_recommended=True),
            'hit': Product.objects.filter(in_hit=True),
            'action': Product.objects.filter(in_action=True),
        }

        for name, queryset in groups.items():
            if not queryset.exists():
                continue
            groups[name] = self.get_pretty_object_list(queryset)

        context['products_groups'] = groups

        return context

    @staticmethod
    def get_pretty_object_list(queryset, b_size=2, box_size=4):

        class Box(object):

            def __init__(self, index):
                super().__init__()

                self._items = []
                self._size = box_size

            @property
            def size(self):
                if not self._items:
                    return 0
                return sum(self.item_size(item) for item in self._items)

            @staticmethod
            def item_size(item):
                return b_size if item.border else 1

            def add(self, item):
                if self.size + self.item_size(item) <= self._size:
                    self._items.append(item)
                    return

                items = self._items.copy()
                items.append(item)
                for comb in permutations(items, len(self._items)):

                    _sum = sum(self.item_size(item) for item in comb)
                    if not _sum == self._size:
                        continue

                    diff = set(self._items).difference(set(comb))

                    self._items = list(comb)

                    try:
                        return diff.pop()
                    except KeyError:
                        return

                return item

            def complete(self):
                return self.size == self._size

        box = None
        count = get_settings('SPECIAL_PRODUCTS_COUNT')
        iteration = 0
        objs = list(queryset.order_by('?')[:count])
        result = []
        while iteration < (count * b_size / box_size):

            if box is None:
                box = Box(iteration)
                box.add(objs.pop(0))

            empty = set()
            for index, item in enumerate(objs):

                obj = box.add(item)
                objs[index] = obj

                if obj is None:
                    empty.add(index)

                if box.complete():
                    break

            for index, pos in enumerate(empty):
                del objs[pos - index]

            if box.complete() or not objs:
                result.append(box._items)
                box = None

            if not objs:
                break

            iteration += 1

        if objs:
            box = box or Box(len(result))
            for orphan in objs:
                box._items.append(orphan)
            result.append(box._items)

        return result


class ProductListView(FilterMixin, SortMixin, SlicePaginatorMixin, ListView):

    model = Product
    paginate_by = 12

    _checked = set()

    def _get_context_data(self, object_list=None):
        context = {'products': object_list}

        context.update(self.get_filter_data())

        context.update(self.get_sort_data(self.queryset))
        context.update(self._sort)

        return context

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():

            html_filter = render_to_string(
                get_template_name('include/catalog_filter.html'),
                context=context, request=self.request)
            html_list = render_to_string(
                get_template_name('include/catalog_group.html'),
                context=context, request=self.request)
            html_paginator = render_to_string(
                'itcase_paginator/include/paginator.html',
                context=context, request=self.request)
            html_sort = render_to_string(
                get_template_name('include/catalog_sort.html'),
                context=context, request=self.request)

            response = {
                'catalog_filter': {'html': html_filter.strip()},
                'catalog_sort': {'html': html_sort.strip()},
                'paginator': {'html': html_paginator.strip()},
                'products_list': {'html': html_list.strip()},
                'query': context.get('query'),
                'sort': context.get('sort'),
                'sort_group': context.get('sort_group'),
            }

            return JsonResponse(response)

        return super().render_to_response(context, **response_kwargs)

    def get_filter_fields(self):
        return Parametr.objects.filter(filter_by=True).values_list(
            'query_name', flat=True)

    def get_filtered_queryset(self, queryset, request):

        queryset = super().get_filtered_queryset(queryset, request).distinct()

        return queryset

    def filter_handle_field(self, model, field, value, _and=True):
        """Extend method FilterMixin.filter_handle_field."""

        if field == 'price_max':
            return Q(**{'prices__price__lte': value}), _and

        if field == 'price_min':
            return Q(**{'prices__price__gte': value}), _and

        if field == 'category':
            if not isinstance(value, list):
                value = [value]

            queryset = Category.objects.filter(pk__in=value)

            _value = []
            for category in queryset:
                descendants = category.get_descendants(include_self=True)
                _value.extend(descendants.values_list('pk', flat=True))
            if _value:
                return Q(**{'category__pk__in': _value}), _and

        if field == 'special':
            return Q(**{'category': value}), _and

        if field in self.get_filter_fields():
            if type(value) is list:
                return Q(**{'parametres__pk__in': value}), _and
            return Q(**{'parametres__pk': value}), _and

        return super().filter_handle_field(model, field, value, _and=_and)

    def get_filter_brand(self):
        _filter = self._filter.get('filter') or {}
        filtered = _filter.get('brand', [])
        single = len(_filter) == 1 and filtered

        queryset = self.get_queryset()

        data = []
        for product in self.queryset:
            if not product.brand:
                continue

            brand = product.brand
            if brand in data:
                continue

            brand.checked = str(brand.pk) in filtered

            enabled = brand.pk in queryset.values_list('brand', flat=True)
            brand.disabled = not enabled and not single

            brand.items_count = queryset.filter(brand=brand).count()

            data.append(brand)
        return data

    def get_filter_category(self):
        if (not hasattr(self, 'object') or
                getattr(self.object, 'level', 0) != 1):
            return

        _filter = self._filter.get('filter') or {}
        filtered = _filter.get('category') or []
        single = len(_filter) == 1 and filtered

        self._checked = set()

        queryset = self.get_queryset()

        data = []
        for category in self.object.children.all():

            checked = str(category.pk) in filtered
            if checked:
                self._checked.add(category.pk)

            category.checked = checked

            descendants = category.get_descendants(include_self=True)
            enabled = queryset.filter(category__in=descendants).exists()
            category.disabled = not enabled and not single

            category.items_count = category.get_products().count()

            data.append(category)

        return data

    def get_filter_special(self):
        if (not hasattr(self, 'object') or
                getattr(self.object, 'level', 0) != 1):
            return

        _filter = self._filter.get('filter') or {}
        filtered = _filter.get('special') or []
        single = len(_filter) == 1 and filtered

        queryset = self.get_queryset()

        data = []
        for category in self.object.get_descendants().filter(level__gt=2):

            category.checked = str(category.pk) in filtered

            descendants = category.get_descendants(include_self=True)
            enabled = queryset.filter(category__in=descendants).exists()
            category.disabled = not enabled and not single

            category.items_count = category.get_products().count()

            data.append(category)

        return data

    def get_filter_price(self):
        filtered = self._filter.get('filter') or {}
        # data = self.queryset.aggregate(Max('price'), Min('price'))
        data = Price.objects.filter(product__in=self.queryset).aggregate(Max('price'), Min('price'))
        initial = {}

        _max = filtered.get('price_max', data.get('price__max'))
        if _max is not None:
            initial['filter_price_max'] = _max

        _min = filtered.get('price_min', data.get('price__min'))
        if _min is not None:
            initial['filter_price_min'] = _min

        return initial

    def get_filter_other_fields(self):
        _filter = self._filter.get('filter') or {}
        data = {}
        queryset = self.get_queryset()

        for field_query_name in self.get_filter_fields():

            field = Parametr.objects.get(query_name=field_query_name)
            picked_parametres = _filter.get(field.query_name, False)

            if type(picked_parametres) is not list:
                picked_parametres = [picked_parametres, ]

            product_parametres = {}
            for parametr in field.product_parametres.all():
                checked = False
                items_count = 0
                items_count = len(
                    parametr.products.intersection(queryset))
                if str(parametr.pk) in picked_parametres:
                    checked = True
                p_data = {'items_count': items_count, 'checked': checked}
                product_parametres[parametr] = p_data

            data[field] = product_parametres

        return data

    def get_filter_data(self):
        initial = {}

        brands = self.get_filter_brand()
        if brands:
            initial['filter_brand'] = brands

        categories = self.get_filter_category()
        if categories:
            initial['filter_category'] = categories

        special = self.get_filter_special()
        if special:
            initial['filter_special'] = special

        initial.update(self.get_filter_price())

        initial['other_fields'] = self.get_filter_other_fields()

        if initial:
            initial['filter_enable'] = True

        return initial

    def get_sort_data(self, queryset):
        initial = {}
        # if queryset.filter(in_hit=True).exists():
        #     initial['in_hit'] = True
        # if queryset.filter(in_action=True).exists():
        #     initial['in_action'] = True
        # if queryset.filter(in_recommended=True).exists():
        #     initial['in_recommended'] = True

        if not initial:
            return {}

        return {'sort_group': initial}


class CategoryDetail(RequestDataMixin, SingleObjectMixin, ProductListView):

    template_name = get_template_name('catalog_groups.html')

    paginator_url_name = 'category-detail'

    def get(self, request, *args, **kwargs):
        queryset = Category.objects.filter(level__lte=1)
        self.object = self.get_object(queryset=queryset)

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        object_list = context.get('object_list')

        if self.hide_products:
            context['categories'] = object_list
        else:
            context.update(self._get_context_data(object_list=object_list))

        context['category'] = self.object

        breadcrumbs = self.object.get_ancestors(include_self=True)
        context['catalog_breadcrumbs'] = breadcrumbs

        return context

    def get_queryset(self):
        if self.hide_products:
            return self.object.children.all()
        self.queryset = self.object.get_products()
        queryset = self.get_filtered_queryset(self.queryset, self.request)
        queryset = self.get_sorted_queryset(queryset, self.request)
        return queryset

    @property
    def hide_products(self):
        if not self.object:
            return False
        return self.object.level == 0 and self.object.children.exists()


class ProductDetail(ProductDetailBase):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        breadcrumbs = self.object.category.get_ancestors(include_self=True)
        context['catalog_breadcrumbs'] = breadcrumbs.filter(level__lte=1)

        context['filter_category'] = breadcrumbs.filter(level=2).first()

        return context
