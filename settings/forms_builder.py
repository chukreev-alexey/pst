# -*- coding: utf-8 -*-

import os

from .filebrowser import FILEBROWSER_DIRECTORY
from .static import MEDIA_ROOT

FORMS_BUILDER_EDITABLE_SLUGS = True
FORMS_BUILDER_UPLOAD_ROOT = os.path.join(MEDIA_ROOT, FILEBROWSER_DIRECTORY)

FORMS_BUILDER_EXTRA_FIELDS = (
    (100, 'captcha.fields.ReCaptchaField', 'ReCaptcha'),
    (101, 'itcase_common.fields.AgreementProcessingPDField',
     'Соглашение на обработку ПД'),
)
