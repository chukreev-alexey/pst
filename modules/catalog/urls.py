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

urlpatterns = [
    path('catalog/', views.CatalogIndexView.as_view(), name='catalog-index'),
    path(
        'category/',
        include([
            path(
                '<slug>/',
                include([
                    path('',
                         views.CategoryDetail.as_view(),
                         name='category-detail'),
                    path('page<int:page>/',
                         views.CategoryDetail.as_view(),
                         name='category-detail'),
                ])),
            path(
                '<parent_slug>/<slug>/',
                include([
                    path('',
                         views.SubCategoryDetail.as_view(),
                         name='subcategory-detail'),
                    path('page<int:page>/',
                         views.SubCategoryDetail.as_view(),
                         name='subcategory-detail'),
                ])),
        ])),
    path('product/<slug>/',
         views.ProductDetail.as_view(),
         name='product-detail'),
]

from .views import foo  # noqa
urlpatterns += [
    path(
        'foo/',
        include([
            path(
                '<slug>/',
                include([
                    path('', foo.FilterView.as_view(), name='foo-category'),
                    path('page<int:page>/',
                         foo.FilterView.as_view(),
                         name='foo-category'),
                ])),
            path(
                '<parent_slug>/<slug>/',
                include([
                    path('',
                         foo.SubCategoryView.as_view(),
                         name='foo-sub-category'),
                    path('page<int:page>/',
                         foo.SubCategoryView.as_view(),
                         name='foo-sub-category'),
                ])),
        ])),
]
