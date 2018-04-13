from django.contrib import admin

from connor.models import WorkoutExcercise, WorkoutPlan


class WorkoutExcerciseInline(admin.TabularInline):
    model = WorkoutExcercise.workout_plan.through
    extra = 0


class WorkoutPlanAdmin(admin.ModelAdmin):
    inlines = [WorkoutExcerciseInline, ]


class WorkoutExcerciseAdmin(admin.ModelAdmin):
    pass


admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(WorkoutExcercise, WorkoutExcerciseAdmin)
