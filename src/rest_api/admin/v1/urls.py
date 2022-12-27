from django.urls import path, include


urlpatterns = [
    path('projects/', include('rest_api.admin.v1.project.urls')),
    path('upload/files/', include('rest_api.admin.v1.file.urls')),
    path('dynamic_export/', include('rest_api.admin.v1.dynamic_export.urls')),
    path('forms/', include('rest_api.admin.v1.form.urls')),
    path('products/', include('rest_api.admin.v1.product.urls')),
]