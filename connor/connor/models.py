from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError


@python_2_unicode_compatible
class WorkoutPlan(models.Model):
    name = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


# Notify User that he has been added to the WorkoutPlan:
def workout_plan_users_changed(sender, **kwargs):
    action = kwargs['action']
    user_ids = kwargs['pk_set']

    if action == 'post_add' and user_ids:
        for user_id in user_ids:
            user = User.objects.get(pk=user_id)

            # this is just for demo purposes:
            send_mail(
                'You have been asigned to a WorkoutPlan!',
                'Hello. You have been asigned to a WorkoutPlan!',
                'connor@example.com',
                [user.email],
                fail_silently=False,
            )


models.signals.m2m_changed.connect(
    workout_plan_users_changed,
    sender=WorkoutPlan.users.through
)


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
        unique=True,
    )

    def __str__(self):
        return self.get_day_display()

    def save(self, *args, **kwargs):
        if WeekDay.objects.count() > 6:
            raise ValidationError('Can only create 7 week day instances')

        super(WeekDay, self).save(*args, **kwargs)


@python_2_unicode_compatible
class WorkoutExcercise(models.Model):
    name = models.CharField(max_length=30, unique=True)
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
