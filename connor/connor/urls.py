from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from connor.views import ListWorkoutPlansView, main

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(
        r'^workout_plans/list$',
        ListWorkoutPlansView.as_view(),
        name='list_workout_plans'
    ),
]
