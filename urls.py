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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from filebrowser.sites import site as fb_site
from rest_framework.authtoken import views as rest_token_views

admin.autodiscover()

urlpatterns = [

    path('admin/', include([
        path('django-rq/', include('django_rq.urls')),
        path('filebrowser/', fb_site.urls),
        path('grappelli/', include('grappelli.urls')),
        path('', include('nested_admin.urls')),
        path('', admin.site.urls),
        path('chaining/', include('smart_selects.urls')),
    ])),

    path('rest/', include([
        path('token/', rest_token_views.obtain_auth_token),
    ])),

    path('', include('website.urls')),
    path('', include('modules.catalog.urls')),

    path('cart/', include('itcase_cart.urls')),
    path('', include('itcase_catalog.urls')),
    path('', include('itcase_feed.urls')),
    path('', include('itcase_gallery.urls')),
    path('', include('itcase_logos.urls')),
    path('search/', include('itcase_search.urls')),
    path('forms/', include('itcase_entry.urls')),

    path('', include('itcase_pages.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
