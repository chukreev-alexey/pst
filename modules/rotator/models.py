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

from mptt.models import TreeManyToManyField

from itcase_rotator.models import RotatorBase
from itcase_common.models.mixins import RELATED_ATTR_NAME

from .conf import get_settings


class Rotator(RotatorBase):

    pages = TreeManyToManyField(get_settings('ITCASE_PAGES_PAGE_MODEL'),
                                related_name=RELATED_ATTR_NAME,
                                verbose_name='Страницы', blank=True)

    class Meta(RotatorBase.Meta):
        db_table = 'itcase_rotator_rotator'
