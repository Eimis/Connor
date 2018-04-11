from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class WorkoutPlan(models.Model):
    name = models.CharField(max_length=30)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


# TODO: data migration
# TODO: limit to 7
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

    day = models.PositiveIntegerField(
        choices=DAYS_OF_WEEK,
        # 1st day of the week:
        default=DAYS_OF_WEEK[0][0],
    )

    def __str__(self):
        return self.get_day_display()

    def save(self, *args, **kwargs):
        if WeekDay.objects.count() > 6:
            raise ValidationError('Can only create 7 week day instances')

        super(WeekDay, self).save(*args, **kwargs)


@python_2_unicode_compatible
class WorkoutExcercise(models.Model):
    name = models.CharField(max_length=30)
    days = models.ManyToManyField(WeekDay, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
