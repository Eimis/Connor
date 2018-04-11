from django.db import models
from django.contrib.auth.models import User


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, blank=True)


# TODO: data migration
# TODO: limit to 7
class WeekDay(models.Model):
    DAYS_OF_WEEK = (
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
        (7, 'Sunday'),
    )

    day = models.PositiveIntegerField(
        choices=DAYS_OF_WEEK,
        # 1st day of the week:
        default=DAYS_OF_WEEK[0][0],
    )


class WorkoutExcercise(models.Model):
    name = models.CharField(max_length=30)
    days = models.ManyToManyField(WeekDay, blank=True)
    description = models.TextField()
