from django.shortcuts import render

from connor.models import WorkoutExcercise, WorkoutPlan
from connor.serializers import WorkoutPlanSerializer

from rest_framework import generics
from rest_framework.response import Response


def main(request):
    '''Main app view for SPA
    '''

    return render(request, 'main.html', {})


class ListWorkoutPlansView(generics.ListAPIView):
    """
    View to list current workout_plans in the system.

    * Requires no authentication
    * Requires no special permissions
    """
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    http_method_names = ['get', ]


class UpdateWorkoutPlanView(generics.UpdateAPIView):
    """
    View to update workout plan.

    * Requires no authentication
    * Requires no special permissions
    """

    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    http_method_names = ['patch', ]

    def patch(self, request, pk):
        workout_plan = self.get_object()

        serializer = WorkoutPlanSerializer(
            workout_plan,
            data=request.data,
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(status=200, data=serializer.data)
        else:
            return Response({pk: serializer.errors}, status=400)


class RemoveWorkoutPlanView(generics.DestroyAPIView):
    """
    View to remove workout plan.

    * Requires no authentication
    * Requires no special permissions
    """

    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
