from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('app_ex.zeus.urls')),
    url(r'^', include('app_ex.hera.urls')),
    url(r'^', include('app_ex.poseidon.urls')),
]
