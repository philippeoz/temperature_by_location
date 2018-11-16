from django.urls import path, include
from django.contrib import admin

from backend.core import urls as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # core app urls
    path('', include(core_urls))
]
