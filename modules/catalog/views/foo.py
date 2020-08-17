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

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, View

from itcase_paginator.pagination import SlicePaginatorMixin

from ..models import Category, Price, Product


class FilterView(View):

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, slug=kwargs['category'])

        data = {}

        filter_query = request.GET.getlist('filter_query')

        price_qs = Price.objects.filter(
            product__category=category).prefetch_related('price_parametres')
        for price in price_qs.iterator():
            params_qs = list(
                price.price_parametres.filter(parametr__filter_by=True))
            for param in params_qs:
                _param = param.parametr_value
                parametr = _param.parametr

                # данные параметра
                filter_key = parametr.pk
                filter_data = data.get(filter_key, {})
                filter_data['name'] = parametr.name
                filter_data['query_name'] = parametr.query_name

                # данные значений параметра
                values = filter_data.get('values', {})
                values_key = _param.pk
                values_data = values.get(values_key, {})
                values_data['name'] = _param.value

                # "связанные" параметры из комплектаций
                scope = values_data.get('scope', [])
                _scope = [
                    item.parametr_value.pk
                    for item in params_qs
                    if item != param
                ]
                scope += _scope
                values_data['scope'] = scope

                # доступен ли пункт при выбранном фильтре
                available = True
                if filter_query:
                    available = any(
                        str(item) in filter_query
                        for item in _scope + [values_key])
                values_data['available'] = available

                values[values_key] = values_data
                filter_data['values'] = values
                data[filter_key] = filter_data

        return JsonResponse(data)


class ProductsListView(SlicePaginatorMixin, ListView):

    context_object_name = 'products'
    model = Product
    paginate_by = 1

    paginator_url_name = 'foo-products'
