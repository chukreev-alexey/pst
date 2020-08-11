# Copyright 2020 ITCase (info@itcase.pro)
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

# ****************************************************************
# PROJECT

PROJECT_NAME = 'pst'

# ****************************************************************
# ITCASE
# Put bellow options for ITCase Dev packages
ITCASE_CATALOG_CATEGORY_MODEL = 'catalog.Category'
ITCASE_CATALOG_PRODUCT_MODEL = 'catalog.Product'

ITCASE_CART_PRODUCT_MODEL = 'catalog.Price'
ITCASE_CART_ORDER_MODEL = 'itcase_cart.Order'
ITCASE_CART_ORDER_ITEM_MODEL = 'itcase_cart.OrderItem'

ITCASE_SEARCH_MODEL_MANAGER_ATTR = 'search_objects'
ITCASE_SEARCH_OBJECTS_PER_PAGE_IN_RESULTS = 9
ITCASE_SEARCH_INDEXABLE_MODELS = [ITCASE_CATALOG_PRODUCT_MODEL]

# django_smart_selects
JQUERY_URL = False
USE_DJANGO_JQUERY = True
