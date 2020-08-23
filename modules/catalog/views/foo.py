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

from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from itcase_paginator.pagination import SlicePaginatorMixin

from ..models import Category, Price, Product, ProductParametr


class FilterView(SlicePaginatorMixin, SingleObjectMixin, ListView):

    context_object_name = 'category'
    template_name = 'foo-category.html'

    paginator_url_name = 'foo-category'

    filter_data = {}
    filter_key_brand = 'filter-brand'
    filter_key_param = 'filter-param'

    def get(self, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())

        self.filter_param_query = []
        for param_query in self.request.GET.getlist('filter-param'):
            try:
                self.filter_param_query.append(int(param_query))
            except (TypeError, ValueError):
                pass

        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_enabled'] = len(self.filter_data) > 0

        context['filter_data_brand'] = self.filter_data[self.filter_key_brand]
        context['filter_key_brand'] = self.filter_key_brand

        context['filter_data_param'] = self.filter_data[self.filter_key_param]
        context['filter_key_param'] = self.filter_key_param

        context['filter_reset_url'] = self.get_filter_reset_url()
        return context

    def get_filter_data(self, queryset):
        data = {}
        filtered_products = []

        _data = {}
        _data, filtered_products = self.get_filter_data_brand(
            queryset, self.request.GET.getlist(self.filter_key_brand))
        if _data:
            data[self.filter_key_brand] = _data

        _data = {}
        products = []
        _data, products = self.get_filter_data_param(
            queryset, self.request.GET.getlist(self.filter_key_param))
        if _data:
            data[self.filter_key_param] = _data
        if filtered_products:
            # если применяли предыдущие фильтры,
            # то берём только то, что совпало у всех фильтров
            filtered_products = [
                pk for pk in products if pk in filtered_products
            ]
        else:
            filtered_products = products

        return data, filtered_products

    def get_filter_data_brand(self, queryset, query):
        data = {}
        filtered_products = []

        for product in self.queryset.select_related('brand'):
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

    def get_filter_data_param(self, queryset, query):

        def get_data(data, params_qs, scope_pks, query, product_id):
            for param in params_qs:
                parametr = param.parametr

                # данные параметра
                filter_key = parametr.pk
                filter_data = data.get(filter_key, {})
                filter_data['name'] = parametr.name

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

                # выбран ли пункт
                values_data['selected'] = values_key in query

                # доступен ли пункт при выбранном фильтре
                available = True
                if query:
                    _scope = scope.copy()
                    _scope.append(values_key)
                    available = all(item in _scope for item in query)
                values_data['available'] = available

                values[values_key] = values_data
                filter_data['values'] = values

                data[filter_key] = filter_data
            return data

        data = {}
        filtered_products = []
        scopes = {}

        price_qs = Price.objects.filter(
            product__in=queryset).prefetch_related('price_parametres')

        # фильтр по параметрам из комплектаций
        for price in price_qs.iterator():
            scope_pks = list(
                price.price_parametres.values_list('parametr_value',
                                                   flat=True))
            scope_pks += list(
                price.product.parametres.values_list('pk', flat=True))
            scope_pks = list(map(str, scope_pks))
            product_id = price.product_id
            scopes[product_id] = scope_pks
            if all(item in scope_pks for item in query):
                filtered_products.append(price.product.pk)

            params_qs = ProductParametr.objects.filter(pk__in=scope_pks)
            data = get_data(data, params_qs, scope_pks, query, product_id)

        # фильтр по параметрам из поля "Параметры"
        for product in queryset.prefetch_related('parametres'):
            params_qs = product.parametres.all()
            scope_pks = scopes.get(
                product.pk, list(params_qs.values_list('pk', flat=True)))
            scope_pks = list(map(str, scope_pks))
            if all(item in scope_pks for item in query):
                filtered_products.append(product.pk)
            data = get_data(data, params_qs, scope_pks, query, product.pk)

        return data, filtered_products

    def get_filter_reset_url(self):
        return reverse(self.paginator_url_name, args=[self.object.slug])

    def get_queryset(self):
        if not self.queryset:
            self.queryset = self.object.products.all()

        queryset = self.queryset

        self.filter_data, filtered_products = self.get_filter_data(queryset)

        if filtered_products:
            queryset = queryset.filter(pk__in=filtered_products).distinct()

            def count_products(iterable, product_pks):
                for item in iterable:
                    item['products'] = [
                        pk for pk in item['products'] if pk in product_pks
                    ]
                    if len(item['products']) < 1:
                        item['available'] = False

            product_pks = queryset.values_list('pk', flat=True)
            for key, _filter in list(self.filter_data.items()):

                if key == self.filter_key_param:
                    for group in list(_filter.values()):
                        count_products(list(group['values'].values()),
                                       product_pks)
                else:
                    count_products(list(_filter.values()), product_pks)

        return queryset


class SubCategoryView(FilterView):

    paginator_url_name = 'foo-sub-category'

    filter_key_category = 'filter-category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_data_category'] = self.filter_data[
            self.filter_key_category]
        context['filter_key_category'] = self.filter_key_category

        return context

    def get_filter_data(self, queryset):
        data, filtered_products = super().get_filter_data(queryset)

        _data = {}
        products = []
        query = self.request.GET.getlist(self.filter_key_category)
        if not query:
            query.append(str(self.object.pk))
        _data, products = self.get_filter_data_category(queryset, query)
        if _data:
            data[self.filter_key_category] = _data
        if filtered_products:
            # если применяли предыдущие фильтры,
            # то берём только то, что совпало у всех фильтров
            filtered_products = [
                pk for pk in products if pk in filtered_products
            ]
        else:
            filtered_products = products

        return data, filtered_products

    def get_filter_data_category(self, queryset, query):
        data = {}
        filtered_products = []

        for product in self.queryset.prefetch_related('categories'):
            categories_qs = product.categories.filter(
                level__gte=self.object.level)
            for category in categories_qs:

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
        return super().get_object(queryset.filter(level__gte=1))

    def get_queryset(self):
        self.queryset = Product.objects.filter(
            categories__in=self.object.parent.children.all())
        return super().get_queryset()
