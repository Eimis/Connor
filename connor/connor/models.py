from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class WorkoutPlan(models.Model):
    # TODO: unique:
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
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

    # TODO: unique:
    day = models.PositiveIntegerField(
        choices=DAYS_OF_WEEK,
        # 1st day of the week:
        default=DAYS_OF_WEEK[0][0],
    )

    def __str__(self):
        return self.get_day_display()

    # TODO proper error message on Admin?
    def save(self, *args, **kwargs):
        if WeekDay.objects.count() > 6:
            raise ValidationError('Can only create 7 week day instances')

        super(WeekDay, self).save(*args, **kwargs)


@python_2_unicode_compatible
class WorkoutExcercise(models.Model):
    # TODO: unique:
    name = models.CharField(max_length=30)
    days = models.ManyToManyField(
        WeekDay,
        blank=True,
        related_name='workout_exercises'
    )
    description = models.TextField()
    workout_plans = models.ManyToManyField(
        WorkoutPlan,
        related_name='workout_exercises'
    )

    def __str__(self):
        return self.name
