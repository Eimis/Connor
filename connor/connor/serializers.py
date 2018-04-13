from django.contrib.auth.models import User

from connor.models import WeekDay, WorkoutExcercise, WorkoutPlan

from rest_framework import serializers


# class WeekDaySerializer(serializers.ModelSerializer):
    # class Meta:
        # model = WeekDay
        # fields = (
            # 'day',
        # )


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()


class WorkoutExcerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutExcercise
        fields = (
            'name',
            # 'days',
            'description',
        )


class WorkoutPlanSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    workout_exercises = WorkoutExcerciseSerializer(many=True)

    class Meta:
        model = WorkoutPlan
        fields = (
            'name',
            'users',
            'workout_exercises',
        )

    def get_different_days(self, obj):
        exercises = obj.workout_exercises.all()
