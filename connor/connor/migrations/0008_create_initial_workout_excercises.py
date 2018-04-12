# Generated by Django 2.0.4 on 2018-04-12 19:33

from django.db import migrations


class Migration(migrations.Migration):
    """A data migration to create initial Workout excercises for the system
    """

    def create_initial_workout_excercises(apps, schema_editor):
        WorkoutExcercise = apps.get_model('connor', 'WorkoutExcercise')

        excercises = [
            {'name': 'Squat', 'description': 'The squat is one of the three \
                                              lifts in the strength sport of \
                                              powerlifting, together with \
                                              deadlifts and bench press'},
            {'name': 'Leg press', 'description': 'The leg press is a weight \
                                                  training exercise in which \
                                                  the individual pushes a \
                                                  weight or resistance away \
                                                  from them using their legs'},
            {'name': 'Lunge', 'description': 'A lunge can refer to any \
                                              position of the human body \
                                              where one leg is positioned \
                                              forward with knee bent and foot \
                                              flat on the ground while the \
                                              other leg is positioned behind'},
            {'name': 'Deadlift', 'description': 'The deadlift is a weight \
                                                 training exercise in which a \
                                                 loaded barbell or bar is \
                                                 lifted off the ground to the \
                                                 level of the hips, then \
                                                 lowered to the ground'},
            {'name': 'Leg extension', 'description': 'The leg extension is a \
                                                      resistance weight \
                                                      training exercise that \
                                                      targets the quadriceps \
                                                      muscle in the legs'},
            {'name': 'Leg curl', 'description': 'The leg curl, also known as \
                                                 the hamstring curl, is an \
                                                 isolation exercise that \
                                                 targets the hamstring \
                                                 muscles'},
            {'name': 'Standing calf raise', 'description': 'Calf raises are a \
                                                            method of \
                                                            exercising the \
                                                            gastrocnemius, \
                                                            tibialis \
                                                            posterior and \
                                                            soleus muscles of \
                                                            the lower leg'},
            {'name': 'Seating calf raise', 'description': 'Calf raises are a \
                                                           method of \
                                                           exercising the \
                                                           gastrocnemius, \
                                                           tibialis posterior \
                                                           and soleus muscles \
                                                           of the lower leg'},
            {'name': 'Hip adductor', 'description': ''},
            {'name': 'Bench press', 'description': 'The bench press is an \
                                                    upper body strength \
                                                    training exercise that \
                                                    consists of pressing a \
                                                    weight upwards from a \
                                                    supine position'},
            {'name': 'Chest fly', 'description': 'The chest fly or pectoral \
                                                  fly (abbreviated to pec \
                                                  fly) primarily works the \
                                                  pectoralis major muscles to \
                                                  move the arms horizontally \
                                                  forward'},
            {'name': 'Push-up', 'description': 'A push-up (or press-up) is a \
                                                common calisthenics exercise \
                                                performed in a prone position \
                                                by raising and lowering the \
                                                body using the arms'},
            {'name': 'Pull-down', 'description': ''},
            {'name': 'Pull-up', 'description': 'A pull-up is an upper-body \
                                                compound pulling exercise'},
            {'name': 'Bent-over row', 'description': 'A bent-over row (or \
                                                      barbell row) is a \
                                                      weight training \
                                                      exercise that targets a \
                                                      variety of back \
                                                      muscles'},
            {'name': 'Shoulder press', 'description': 'The press, overhead \
                                                       press or shoulder \
                                                       press is a weight \
                                                       training exercise, \
                                                       typically performed \
                                                       while standing, in \
                                                       which a weight is \
                                                       pressed straight \
                                                       upwards from racking \
                                                       position until the \
                                                       arms are locked out \
                                                       overhead'},
            {'name': 'Lateral raise', 'description': 'The shoulder fly (also \
                                                      known as a lateral \
                                                      raise) works the \
                                                      deltoid muscle of the \
                                                      shoulder'},
            {'name': 'Shoulder shrug', 'description': 'The shoulder shrug \
                                                       (usually called simply \
                                                       the shrug) is an \
                                                       exercise in weight \
                                                       training used to \
                                                       develop the upper \
                                                       trapezius muscle'},
            {'name': 'Pushdown', 'description': 'A pushdown is a strength \
                                                 training exercise used for \
                                                 strengthening the triceps \
                                                 muscles in the back of the \
                                                 arm'},
            {'name': 'Russian twist', 'description': 'The Russian twist is a \
                                                      type of exercise that \
                                                      is used to work the \
                                                      abdominal muscles by \
                                                      performing a twisting \
                                                      motion on the abdomen.'},
        ]

        for e in excercises:
            we = WorkoutExcercise.objects.create(
                name=e['name'],
                description=e['description']
            )

            print('\nCreated initial Workout excercise: {0}'.format(we.name))

    def remove_initial_workout_excercises(apps, schema_editor):
        pass

    dependencies = [
        ('connor', '0007_assign_initial_workout_plans'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_workout_excercises,
            remove_initial_workout_excercises
        ),
    ]
