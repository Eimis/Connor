# Generated by Django 2.0.4 on 2018-04-12 18:29

from django.db import migrations


class Migration(migrations.Migration):
    """A data migration to create initial Workout plans for the system
    """

    def create_initial_workout_plans(apps, schema_editor):
        WorkoutPlan = apps.get_model('connor', 'WorkoutPlan')

        # 1. Create workout plans:
        plan1 = WorkoutPlan.objects.create(
            name="'7 day weight loss' plan",
        )
        plan2 = WorkoutPlan.objects.create(
            name="The 'starting strength' program",
        )
        plan3 = WorkoutPlan.objects.create(
            name='A plan for absolute beginners',
        )
        plan4 = WorkoutPlan.objects.create(
            name='Workout plan for middle-aged females',
        )
        plan5 = WorkoutPlan.objects.create(
            name='Intermediate weightlifter workout routine',
        )

        for plan in [plan1, plan2, plan3, plan4, plan5]:
            print('\nCreated initial Workout plan: {0}'.format(plan.name))

    def remove_initial_workout_plans(apps, schema_editor):
        pass

    dependencies = [
        ('connor', '0005_create_initial_users'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_workout_plans,
            remove_initial_workout_plans
        ),
    ]
