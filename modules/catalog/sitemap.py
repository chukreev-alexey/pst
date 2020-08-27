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

from django.db.models import Max

from itcase_common.utils import BaseSitemap

__all__ = ('CategorySitemap', 'ProductSitemap', 'sitemaps')


class CategorySitemap(BaseSitemap):
    """Sitemap class for Categories."""

    def items(self):
        """Return active pages for SiteMap."""
        from itcase_catalog.shortcuts import get_category_model

        return get_category_model().objects.all()

    def priority(self, obj):
        """Set max priority for root nodes."""
        return float(pow(0.9, obj.level + 1))


class ProductSitemap(BaseSitemap):
    """Sitemap class for Products."""

    def items(self):
        """Return active pages for SiteMap."""
        from itcase_catalog.shortcuts import get_product_model

        return get_product_model().objects.annotate(
            category_max_level=Max('categories__level'))

    def priority(self, obj):
        """Set max priority for root nodes."""
        level = obj.category_max_level if obj.category_max_level else 2
        return float(pow(0.9, level + 1))


sitemaps = {}
sitemaps['categories'] = CategorySitemap
sitemaps['products'] = ProductSitemap
