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

from appconf import AppConf

from .apps import CatalogConfig

__all__ = ['CatalogAppConf', 'get_settings', 'PREFIX']

PREFIX = CatalogConfig.label


def get_settings(name, default=None):
    from itcase_common.utils import get_settings as getter

    return getter(name, prefix=PREFIX.upper(), default=default)


class CatalogAppConf(AppConf):
    from datetime import timedelta

    SPECIAL_PRODUCTS_COUNT = 7

    class Meta(object):

        prefix = PREFIX
