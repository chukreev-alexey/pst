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

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()

from .cache import CACHES  # noqa
from .core import *  # noqa
from .logging import LOGGING  # noqa
from .static import *  # noqa

from .compressor import *  # noqa
from .filebrowser import *  # noqa
from .forms_builder import *  # noqa
from .grappelli import *  # noqa
from .recaptcha import *  # noqa
from .rest_framework import REST_FRAMEWORK  # noqa
from .rq import RQ_QUEUES  # noqa

from .project import *  # noqa

from .local import *  # noqa
