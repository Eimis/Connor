from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from connor.views import ListWorkoutPlansView, main, UpdateWorkoutPlanView

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
        name='update_issue'
    ),
]
