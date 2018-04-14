from django.contrib.auth.models import User

from connor.models import WorkoutExcercise, WorkoutPlan

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'pk',
            'full_name',
        )

    def get_full_name(self, obj):
        return obj.get_full_name()


class WorkoutExcerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkoutExcercise
        fields = (
            'pk',
            'name',
            'description',
        )


class WorkoutPlanSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, required=False)
    workout_exercises = WorkoutExcerciseSerializer(many=True, required=False)
    all_exercises = serializers.SerializerMethodField()
    all_users = serializers.SerializerMethodField()

    class Meta:
        model = WorkoutPlan
        fields = (
            'pk',
            'name',
            'users',
            'all_users',
            'workout_exercises',
            'all_exercises',
        )

    def get_all_exercises(self, obj):
        all_exercises = WorkoutExcercise.objects.all().order_by('name')

        return WorkoutExcerciseSerializer(all_exercises, many=True).data

    def get_all_users(self, obj):
        all_users = User.objects.all().order_by('first_name')

        return UserSerializer(all_users, many=True).data

    # because of complex m2m relationships, we have to override this method,
    # see: http://www.django-rest-framework.org/api-guide/serializers/#writing-update-methods-for-nested-representations  # NOQA: E501
    # TODO: separate methods?
    def update(self, instance, validated_data):

        # shortcut to clear m2m relationships if no data was posted:
        posted_users = [
            x['pk'] for x in self.initial_data['users']
        ]
        if not posted_users:
            instance.users.clear()

        # XXX: for some reason while updating complex m2m relationships, DRF
        # is returning empty dictionary for validated_data, although is_valid()
        # returns True. This is safe, because is_valid() has already been
        # called and because of the scope of this task, we're leaving this as
        # a FIXME:
        users_valid = self.is_valid() and not all([
            bool(x) for x in self.validated_data['users']
        ])

        if users_valid:
            existing_users = [
                x.pk for x in instance.users.all()
            ]

            for eu in existing_users:
                if eu not in posted_users:
                    instance.users.remove(eu)

            instance.users.add(*posted_users)

        # shortcut to clear m2m relationships if no data was posted:
        posted_exercises = [
            x['pk'] for x in self.initial_data['workout_exercises']
        ]
        if not posted_exercises:
            instance.workout_exercises.clear()

        exercises_valid = self.is_valid() and not all([
            bool(x) for x in self.validated_data['workout_exercises']
        ])

        if exercises_valid:
            existing_exercises = [
                x.pk for x in instance.workout_exercises.all()
            ]

            for ee in existing_exercises:
                if ee not in posted_exercises:
                    instance.workout_exercises.remove(ee)

            instance.workout_exercises.add(*posted_exercises)

        instance.name = validated_data.get('name', instance.name)

        instance.save()

        return instance
