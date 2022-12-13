"""activation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.debug import default_urlconf
from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi, generators
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view as get_schema_views
from django.http import JsonResponse
from django.views.generic.base import RedirectView
import os

class BothHttpAndHttpsSchemaGenerator(generators.OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ['http', 'https'] if bool(True) else ['https', 'http']
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
        validators=['ssv', 'flex'],

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url="https://localhost"
    generator_class=BothHttpAndHttpsSchemaGenerator,
)

mobile_schema_view = get_schema_view(
    openapi.Info(
        title="Activation Mobile API",
        default_version="v1.1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
        validators=['ssv', 'flex'],

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url="",
    patterns=[
        path('mobile/api/v1/', include('rest_api.mobile.v1.urls')),
    ],
    generator_class=BothHttpAndHttpsSchemaGenerator,
)

admin_schema_view = get_schema_view(
    openapi.Info(
        title="Activation CMS API",
        default_version="v1.1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
        validators=['ssv', 'flex'],

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # url="",
    patterns=[
        path('admin/api/v1/', include('rest_api.admin.v1.urls')),
    ],
    generator_class=BothHttpAndHttpsSchemaGenerator,
)

urlpatterns = [
    path('admincp/', admin.site.urls),
    path('admin/api/v1/', include('rest_api.admin.v1.urls')),
    path('mobile/api/v1/', include('rest_api.mobile.v1.urls')),
]


# For Development
if bool(True):
    urlpatterns += [
        path('docs/', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
        path('docs/admin/', admin_schema_view.with_ui('swagger',
                cache_timeout=0), name='schema-swagger-ui'),
        path('docs/mobile', mobile_schema_view.with_ui('swagger',
                cache_timeout=0), name='schema-swagger-ui'),
        path('__debug__/', include('debug_toolbar.urls')),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)