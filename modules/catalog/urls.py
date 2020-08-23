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

from django.urls import include, path

from . import views
from .views import foo  # noqa

urlpatterns = [
    path('catalog/', views.CatalogIndexView.as_view(), name='catalog-index'),
    path(
        'category/',
        include([
            path(
                '<slug>/',
                include([
                    path('',
                         foo.CategoryDetail.as_view(),
                         name='category-detail'),
                    path('page<int:page>/',
                         foo.CategoryDetail.as_view(),
                         name='category-detail'),
                ])),
            path(
                '<parent_slug>/<slug>/',
                include([
                    path('',
                         foo.SubCategoryDetail.as_view(),
                         name='subcategory-detail'),
                    path('page<int:page>/',
                         foo.SubCategoryDetail.as_view(),
                         name='subcategory-detail'),
                ])),
        ])),
    path('product/<slug>/',
         views.ProductDetail.as_view(),
         name='product-detail'),
]
