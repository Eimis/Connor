from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from connor.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', main, name='main'),
]
