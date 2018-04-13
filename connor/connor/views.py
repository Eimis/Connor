from django.shortcuts import render

from connor.models import WorkoutPlan
from connor.serializers import WorkoutPlanSerializer

from rest_framework import generics


def main(request):
    '''Main app view for SPA
    '''

    return render(request, 'main.html', {})


class ListWorkoutPlansView(generics.ListAPIView):
    """
    View to list current issues in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    http_method_names = ['get', ]
