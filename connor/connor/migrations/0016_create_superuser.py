# Generated by Django 2.0.4 on 2018-04-15 10:48

from django.contrib.auth.models import User
from django.db import migrations


class Migration(migrations.Migration):

    def create_initial_superuser(apps, schema_editor):
        SUPERUSER_PASSWORD = 'superuser'

        su = User.objects.create_user(
            username='superuser',
            first_name='Superuser',
            last_name='Smith',
            email='superuser@example.com',
            is_staff=True,
            is_superuser=True,
        )
        su.set_password(SUPERUSER_PASSWORD)
        su.save()

        print('\nCreated initial superuser account: {0} / {1}'.format(
            su.username, SUPERUSER_PASSWORD
        ))

    def remove_initial_superuser(apps, schema_editor):
        pass

    dependencies = [
        ('connor', '0015_auto_20180414_1542'),
    ]

    operations = [
        migrations.RunPython(
            create_initial_superuser,
            remove_initial_superuser
        ),
    ]
