from django.contrib.auth.models import User
from django.shortcuts import render

from connor.models import WorkoutExcercise, WorkoutPlan
from connor.serializers import WorkoutPlanSerializer, UserSerializer, \
    WorkoutExcerciseSerializer

from rest_framework import generics
from rest_framework import views
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


class CreateWorkoutPlanView(generics.CreateAPIView):
    """
    View to create workout plan.

    * Requires no authentication
    * Requires no special permissions
    """

    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer


class ExtraDataView(views.APIView):
    """
    View to get extra data for frontend.

    * Requires no authentication
    * Requires no special permissions

    * Returns a list of all available Users
    * Returns a list of all available WorkoutExcercises
    """
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

    http_method_names = ['get', ]

    def get(self, request):
        all_users = User.objects.all()
        all_exercises = WorkoutExcercise.objects.all()

        user_serializer = UserSerializer(all_users, many=True)
        exercise_serializer = WorkoutExcerciseSerializer(
            all_exercises,
            many=True
        )

        return Response({
            'all_users': user_serializer.data,
            'all_exercises': exercise_serializer.data,
        })
