from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('app_ex.Sif.urls')),
    url(r'^', include('app_ex.Frigga.urls')),
    url(r'^', include('app_ex.Loki.urls')),
    url(r'^', include('app_ex.Thor.urls')),
    url(r'^', include('app_ex.Odin.urls')),
]
