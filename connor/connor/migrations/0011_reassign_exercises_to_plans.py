# Generated by Django 2.0.4 on 2018-04-13 12:32
import random

from django.db import migrations


class Migration(migrations.Migration):
    """A data migration to re-asign exercises to some Workout plans, because
    when ForeignKey relationship was changed to m2m, related data was lost
    """

    def assign_exercises_to_plans(apps, schema_editor):
        WorkoutExcercise = apps.get_model('connor', 'WorkoutExcercise')
        WorkoutPlan = apps.get_model('connor', 'WorkoutPlan')

        plans = WorkoutPlan.objects.all()
        exercises = WorkoutExcercise.objects.all()

        for wp in plans:

            # Choose a random number of WeekDays:
            number_of_exercises_to_add = random.randint(
                0, exercises.count()
            )
            random_exercises = random.sample(
                list(exercises), number_of_exercises_to_add
            )

            wp.workoutexcercise_set.add(*random_exercises)

        print('\nRandomly re-assigned exercises to Workout plans')

    def unassign_exercises_from_plans():
        pass

    dependencies = [
        ('connor', '0010_auto_20180413_1227'),
    ]

    operations = [
        migrations.RunPython(
            assign_exercises_to_plans,
            unassign_exercises_from_plans,
        ),
    ]