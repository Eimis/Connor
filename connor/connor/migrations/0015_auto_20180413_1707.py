# Generated by Django 2.0.4 on 2018-04-13 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connor', '0014_auto_20180413_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workoutplan',
            old_name='user',
            new_name='users',
        ),
    ]
