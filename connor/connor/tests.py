import json

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from connor.models import WorkoutExcercise, WorkoutPlan


class WorkoutPlansAPITestCase(TestCase):

    def test_main_view(self):
        """
        Tests if main app view returns proper status code
        """

        url = reverse('main')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_workout_plan_view(self):

        """
        Tests if this API endpoint properly updates Workout Plan model instance
        """
        # This WorkoutPlan is created during data migration, but later on one
        # might want to use factory_boy or similar library:
        workout_plan = WorkoutPlan.objects.first()

        # These were created during data migration, but later on one might
        # want to use factory_boy or similar library:
        john_doe = User.objects.get(username='john_doe')
        linda_doe = User.objects.get(username='linda_doe')
        lunge_exercise = WorkoutExcercise.objects.get(pk=3)

        self.assertTrue(workout_plan.name)
        self.assertTrue(john_doe in workout_plan.users.all())
        self.assertFalse(linda_doe in workout_plan.users.all())

        # exercises are asigned randomly during mygrations so we can't check
        # pre-existing exercise relationships

        NEW_WORKOUT_PLAN_NAME = 'New name'
        self.assertFalse(workout_plan.name == NEW_WORKOUT_PLAN_NAME)

        post_data = {
            'name': NEW_WORKOUT_PLAN_NAME,
            'users': [{'pk': linda_doe.pk}, ],
            'workout_exercises': [{'pk': lunge_exercise.pk}, ],
        }

        response = self.client.patch(
            reverse('update_workout_plan', kwargs={'pk': workout_plan.pk}),
            json.dumps(post_data),
            content_type='application/json',
        )

        self.assertEqual(response.status_code, 200)
        workout_plan.refresh_from_db()

        self.assertEquals(workout_plan.name, NEW_WORKOUT_PLAN_NAME)
        self.assertTrue(linda_doe in workout_plan.users.all())
        self.assertFalse(john_doe in workout_plan.users.all())
        self.assertEqual(workout_plan.users.all().count(), 1)

        self.assertTrue(lunge_exercise in workout_plan.workout_exercises.all())
        self.assertEqual(workout_plan.workout_exercises.all().count(), 1)
