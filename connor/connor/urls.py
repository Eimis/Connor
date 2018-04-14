from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from connor.views import CreateWorkoutPlanView, ExtraDataView, \
    ListWorkoutPlansView, main, RemoveWorkoutPlanView, UpdateWorkoutPlanView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(
        r'^workout_plans/list$',
        ListWorkoutPlansView.as_view(),
        name='list_workout_plans'
    ),
    url(
        r'^workout_plans/(?P<pk>\d+)/update$',
        UpdateWorkoutPlanView.as_view(),
        name='update_workout_plan'
    ),
    url(
        r'^workout_plans/(?P<pk>\d+)/remove$',
        RemoveWorkoutPlanView.as_view(),
        name='update_workout_plan'
    ),
    url(
        r'^workout_plans/create$',
        CreateWorkoutPlanView.as_view(),
        name='create_workout_plan'
    ),
    url(
        r'^workout_plans/extra_data$',
        ExtraDataView.as_view(),
        name='extra_data'
    ),
]
