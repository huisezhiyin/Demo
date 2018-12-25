from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('app_ex.zeus.urls')),
]
