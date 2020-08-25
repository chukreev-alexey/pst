# Copyright 2020 Petr Zelenin (po.zelenin@itcase.pro)
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

from django.db.models import Max, Min
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from itcase_catalog.conf import get_template_name
from itcase_common.mixins import SortMixin
from itcase_paginator.pagination import SlicePaginatorMixin

from ..models import Category, Price, Product


class CategoryDetail(SlicePaginatorMixin, SortMixin, SingleObjectMixin,
                     ListView):

    context_object_name = 'category'
    template_name = get_template_name('catalog_groups.html')

    paginator_url_name = 'category-detail'

    filter_data = {}
    filter_key_brand = 'filter-brand'
    filter_key_misc = 'filter-misc'
    filter_key_param = 'filter-param-'
    filter_key_price = 'filter-price-'
    filter_query_dict = {}

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.filter(
            level__lte=1))

        if self.object.other_template:
            self.template_name = get_template_name('other_catalog_groups.html')

        self.filter_query_dict[self.filter_key_brand] = request.GET.getlist(
            self.filter_key_brand)
        self.filter_query_dict[self.filter_key_misc] = request.GET.getlist(
            self.filter_key_misc)

        self.filter_query_dict[self.filter_key_param] = {
            k.replace(self.filter_key_param, ''): v
            for k, v in request.GET.lists()
            if k.startswith(self.filter_key_param)
        }

        self.filter_query_dict[self.filter_key_price] = {
            k.replace(self.filter_key_price, ''): v
            for k, v in request.GET.items()
            if k.startswith(self.filter_key_price) and v
        }

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['catalog_breadcrumbs'] = self.object.get_ancestors(
            include_self=True)

        context['products'] = context['page_obj']

        if self.hide_products:
            context['categories'] = context['page_obj']
        else:
            context['filter_enabled'] = len(self.filter_data) > 0

            context['filter_data_brand'] = self.filter_data.get(
                self.filter_key_brand)
            context['filter_key_brand'] = self.filter_key_brand

            context['filter_data_misc'] = self.filter_data.get(
                self.filter_key_misc)
            context['filter_key_misc'] = self.filter_key_misc

            context['filter_data_param'] = self.filter_data.get(
                self.filter_key_param)
            context['filter_key_param'] = self.filter_key_param

            context['filter_data_price'] = self.filter_data.get(
                self.filter_key_price)
            context['filter_key_price'] = self.filter_key_price

            context['filter_reset_url'] = self.get_filter_reset_url()

            context.update(self.get_sort_data(self.queryset))
            context.update(self._sort)

        return context

    def get_filter_data(self, queryset):
        data = {}
        filtered_products = {}

        _data = {}
        products = []
        _data, products = self.get_filter_data_brand(
            queryset, self.filter_query_dict.get(self.filter_key_brand))
        if _data:
            data[self.filter_key_brand] = _data
        if products:
            filtered_products[self.filter_key_brand] = products
            filtered_products['final'] = products

        _data = {}
        products = []
        _data, products = self.get_filter_data_misc(
            queryset, self.filter_query_dict.get(self.filter_key_misc))
        if _data:
            data[self.filter_key_misc] = _data
        if products:
            filtered_products[self.filter_key_misc] = products
            if 'final' not in filtered_products:
                filtered_products['final'] = products
            else:
                filtered_products['final'] = [
                    pk for pk in products if pk in filtered_products['final']
                ]

        _data = {}
        products = []
        _data, products = self.get_filter_data_param(
            queryset, self.filter_query_dict.get(self.filter_key_param))
        if _data:
            data[self.filter_key_param] = _data
        if products:
            filtered_products[self.filter_key_param] = products

            products = [pk for value in products.values() for pk in value]
            if 'final' not in filtered_products:
                filtered_products['final'] = products
            else:
                filtered_products['final'] = [
                    pk for pk in products if pk in filtered_products['final']
                ]

        _data = {}
        products = []
        _data, products = self.get_filter_data_price(
            queryset, self.filter_query_dict.get(self.filter_key_price))
        if _data:
            data[self.filter_key_price] = _data
        if products:
            filtered_products[self.filter_key_price] = products
            if 'final' not in filtered_products:
                filtered_products['final'] = products
            else:
                filtered_products['final'] = [
                    pk for pk in products if pk in filtered_products['final']
                ]

        return data, filtered_products

    def get_filter_data_brand(self, queryset, query):
        data = {}
        filtered_products = []

        for product in self.queryset:
            brand = product.brand
            if brand is None:
                continue

            # данные бренда
            filter_key = str(brand.pk)
            filter_data = data.get(filter_key, {})
            filter_data['name'] = brand.name

            # товары в которых есть этот бренд
            products = filter_data.get('products', set())
            products.add(product.pk)
            filter_data['products'] = products

            # доступен ли пункт при выбранном фильтре
            filter_data['available'] = product in queryset

            # выбран ли пункт
            selected = filter_key in query
            if selected:
                filtered_products.append(product.pk)
            filter_data['selected'] = selected

            data[filter_key] = filter_data

        return data, filtered_products

    def get_filter_data_misc(self, queryset, query):
        data = {}
        filtered_products = []

        for key in ('in_hit', 'in_action', 'in_recommended'):
            if not self.queryset.filter(**{key: True}).exists():
                continue
            products = queryset.filter(**{key: True})
            product_pks = list(products.values_list('pk', flat=True))
            selected = key in query
            data[key] = {
                'products': product_pks,
                'available': products.exists(),
                'selected': selected
            }
            if selected:
                filtered_products += product_pks

        return data, filtered_products

    def get_filter_data_param(self, queryset, query):
        data = {}
        filtered_products = {}
        scopes = {}

        price_qs = Price.objects.filter(
            product__in=queryset,
            show=True).select_related('product').prefetch_related(
                'price_parametres__parametr_value__parametr',
                'product__parametres__parametr')

        for price in price_qs:
            params_qs = []
            scope_pks = []
            # параметры из комплектаций
            for price_parametr in price.price_parametres.all():
                param = price_parametr.parametr_value
                if not param.parametr.filter_by:
                    continue
                params_qs.append(param)
                scope_pks.append(str(param.pk))

            # параметры из поля "Параметры" у товара
            for param in price.product.parametres.all():
                if not param.parametr.filter_by:
                    continue
                params_qs.append(param)
                scope_pks.append(str(param.pk))

            product_id = price.product_id
            scopes[product_id] = scope_pks

            for param in params_qs:
                parametr = param.parametr

                # данные параметра
                filter_key = parametr.pk
                filter_data = data.get(filter_key, {})
                filter_data['name'] = parametr.name

                query_name = parametr.query_name
                filter_data['query_name'] = query_name

                # данные значений параметра
                values = filter_data.get('values', {})
                values_key = str(param.pk)
                values_data = values.get(values_key, {})
                values_data['name'] = param.value

                # товары в которых есть этот параметр
                products = values_data.get('products', set())
                products.add(product_id)
                values_data['products'] = products

                # "связанные" параметры из комплектаций
                scope = list(values_data.get('scope', []))
                _scope = [pk for pk in scope_pks if pk != values_key]
                scope += _scope
                values_data['scope'] = set(scope)

                _query = query.get(query_name, [])

                # выбран ли пункт
                selected = values_key in _query
                values_data['selected'] = selected
                if selected:
                    _filtered_products = filtered_products.get(query_name, [])
                    _filtered_products.append(product_id)
                    filtered_products[query_name] = _filtered_products

                # доступен ли пункт при выбранном фильтре
                available = True
                if not _query:
                    _scope = scope.copy()
                    _scope.append(values_key)
                    available = all(item in _scope for item in _query)
                values_data['available'] = available

                values[values_key] = values_data
                filter_data['values'] = values

                data[filter_key] = filter_data

        data = {
            k: v
            for k, v in sorted(list(data.items()), key=lambda i: i[1]['name'])
        }
        for value in data.values():
            value['values'] = {
                k: v
                for k, v in sorted(list(value['values'].items()),
                                   key=lambda i: i[1]['name'])
            }

        return data, filtered_products

    def get_filter_data_price(self, queryset, query):
        price_qs = Price.objects.filter(product__in=queryset)

        _data = price_qs.aggregate(Max('price'), Min('price'))
        data = dict((key, _data[f'price__{key}']) for key in ('max', 'min'))

        filtered_products = []
        if query:
            filtered_products = list(
                price_qs.filter(price__lte=query['max'],
                                price__gte=query['min']).values_list(
                                    'product_id', flat=True))

        return data, filtered_products

    def get_filter_reset_url(self):
        return reverse(self.paginator_url_name, args=[self.object.slug])

    def get_queryset(self):
        if self.hide_products:
            return self.object.get_children_not_empty()

        if not self.queryset:
            self.queryset = self.object.products.all()

        self.queryset = self.queryset.select_related('brand').prefetch_related(
            'categories')

        self.queryset = self.get_sorted_queryset(self.queryset, self.request)

        if self.object.other_template:
            return self.queryset

        queryset = self.queryset

        self.filter_data, filtered_products = self.get_filter_data(queryset)

        if 'final' not in filtered_products:
            return queryset

        queryset = queryset.filter(pk__in=filtered_products['final'])

        def count_products(iterable, product_pks):
            for item in iterable:
                if not item['available']:
                    item['products'] = []
                    continue
                item['products'] = [
                    pk for pk in item['products'] if pk in product_pks
                ]
                if len(item['products']) < 1:
                    item['available'] = False
                    item['selected'] = False

        final = filtered_products.pop('final', None)

        for key, _filter in list(self.filter_data.items()):
            product_pks = []
            if final:
                for k, v in filtered_products.items():
                    if k in (key, 'final'):
                        continue
                    if k == self.filter_key_param:
                        v = [pk for value in v.values() for pk in value]
                    if not product_pks:
                        product_pks = v
                    else:
                        product_pks = [pk for pk in v if pk in product_pks]

            if key.startswith(self.filter_key_param):
                for group in list(_filter.values()):
                    _filtered_products = filtered_products.get(key, {})
                    for k, v in _filtered_products.items():
                        if k == group['query_name']:
                            continue
                        product_pks = [pk for pk in v if pk in product_pks]
                    count_products(list(group['values'].values()), product_pks)
                continue

            if key.startswith(self.filter_key_price):
                continue

            if len(filtered_products) == 1 and key in filtered_products:
                product_pks = self.queryset.values_list('pk', flat=True)

            count_products(list(_filter.values()), product_pks)

        return queryset.distinct()

    def get_sort_data(self, queryset):
        initial = {}

        for key in ('in_hit', 'in_action', 'in_recommended'):
            initial[key] = queryset.filter(**{key: True}).exists()

        if any(initial.values()):
            return {'sort_group': initial}

        return {}

    def get_sorted_queryset(self, queryset, request, **kwargs):

        params = getattr(request, request.method, {})
        _sort = self.handle_query_sort(queryset.model, params, **kwargs)

        if _sort:
            if 'price' in _sort or '-price' in _sort:
                # сортировка по минимальному значению в m2m поле prices
                if 'price' in _sort:
                    _sort.remove('price')
                    _sort += ['lowest_price']
                if '-price' in _sort:
                    _sort.remove('-price')
                    _sort += ['-lowest_price']
                return queryset.annotate(
                    lowest_price=Min('prices__price')).order_by(*_sort)
            return queryset.order_by(*_sort)

        return queryset

    @property
    def hide_products(self):
        if self.object:
            return self.object.level == 0 and self.object.children.exists()
        return False

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():

            html_filter = render_to_string(
                get_template_name('include/catalog_filter.html'),
                context=context,
                request=self.request)
            html_list = render_to_string(
                get_template_name('include/catalog_group.html'),
                context=context,
                request=self.request)
            html_paginator = render_to_string(
                'itcase_paginator/include/paginator.html',
                context=context,
                request=self.request)
            html_sort = render_to_string(
                get_template_name('include/catalog_sort.html'),
                context=context,
                request=self.request)

            response = {
                'catalog_filter': {
                    'html': html_filter.strip()
                },
                'catalog_sort': {
                    'html': html_sort.strip()
                },
                'paginator': {
                    'html': html_paginator.strip()
                },
                'products_list': {
                    'html': html_list.strip()
                },
                'query': context.get('query'),
                'sort': context.get('sort'),
                'sort_group': context.get('sort_group'),
            }

            return JsonResponse(response)

        return super().render_to_response(context, **response_kwargs)


class SubCategoryDetail(CategoryDetail):

    paginator_url_name = 'subcategory-detail'

    filter_key_category = 'filter-category'

    def get(self, request, *args, **kwargs):
        self.filter_query_dict[self.filter_key_category] = request.GET.getlist(
            self.filter_key_category)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.hide_products:
            context['filter_data_category'] = self.filter_data.get(
                self.filter_key_category)
            context['filter_key_category'] = self.filter_key_category

        return context

    def get_filter_data(self, queryset):
        data, filtered_products = super().get_filter_data(queryset)

        _data = {}
        products = []
        query = self.filter_query_dict.get(self.filter_key_category)
        if not any(value for value in self.filter_query_dict.values()):
            query.append(str(self.object.pk))
            self.filter_query_dict[self.filter_key_category] = query
        _data, products = self.get_filter_data_category(queryset, query)
        if _data:
            data[self.filter_key_category] = _data
        if products:
            filtered_products[self.filter_key_category] = products
            if 'final' not in filtered_products:
                filtered_products['final'] = products
            else:
                # если применяли предыдущие фильтры,
                # то берём только то, что совпало у всех фильтров
                filtered_products['final'] = [
                    pk for pk in products if pk in filtered_products['final']
                ]

        return data, filtered_products

    def get_filter_data_category(self, queryset, query):
        data = {}
        filtered_products = []

        for product in self.queryset:
            for category in product.categories.all():
                if category.level < self.object.level:
                    continue

                # данные категории
                filter_key = str(category.pk)
                filter_data = data.get(filter_key, {})
                filter_data['name'] = category.name

                # товары в которых есть эта категория
                products = filter_data.get('products', set())
                products.add(product.pk)
                filter_data['products'] = products

                # доступен ли пункт при выбранном фильтре
                filter_data['available'] = product in queryset

                # выбран ли пункт
                selected = filter_key in query
                if selected:
                    filtered_products.append(product.pk)
                filter_data['selected'] = selected

                data[filter_key] = filter_data

        return data, filtered_products

    def get_filter_reset_url(self):
        return reverse(self.paginator_url_name,
                       args=[self.object.parent.slug, self.object.slug])

    def get_object(self, queryset):
        return super().get_object(Category.objects.filter(level__gte=1))

    def get_queryset(self):
        self.queryset = Product.objects.filter(
            categories__in=self.object.parent.children.all())
        return super().get_queryset()
