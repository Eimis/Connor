# Generated by Django 2.0.4 on 2018-04-12 20:14
import random

from django.db import migrations


class Migration(migrations.Migration):
    """A data migration to set initial days for Workout exercises and asign
    exercises to some Workout plans
    """

    def set_days_and_plans(apps, schema_editor):
        WeekDay = apps.get_model('connor', 'WeekDay')
        WorkoutExcercise = apps.get_model('connor', 'WorkoutExcercise')
        WorkoutPlan = apps.get_model('connor', 'WorkoutPlan')

        # these were created during precious data migrations:
        days = WeekDay.objects.all()
        plans = WorkoutPlan.objects.all()
        exercises = WorkoutExcercise.objects.all()

        def _set_days_for_exercises():

            for we in exercises:

                # Choose a random number of WeekDays:
                number_of_weekdays_to_add = random.randint(0, 7)
                random_days = random.sample(
                    list(days), number_of_weekdays_to_add
                )

                we.days.add(*random_days)

            print('\nRandomly assigned weekdays to Workout excercises')

        def _assign_exercises_to_plans():

            for wp in plans:

                # Choose a random number of WeekDays:
                number_of_exercises_to_add = random.randint(
                    0, exercises.count()
                )
                random_exercises = random.sample(
                    list(exercises), number_of_exercises_to_add
                )

                wp.workoutexcercise_set.add(*random_exercises)

            print('\nRandomly assigned exercises to Workout plans')

        _set_days_for_exercises()
        _assign_exercises_to_plans()

    def unset_days_and_plans():
        pass

    dependencies = [
        ('connor', '0008_create_initial_workout_excercises'),
    ]

    operations = [
        migrations.RunPython(
            set_days_and_plans,
            unset_days_and_plans,
        ),
    ]
