from django.contrib import admin

from connor.models import WorkoutExcercise, WorkoutPlan


class WorkoutPlanAdmin(admin.ModelAdmin):
    pass


class WorkoutExcerciseAdmin(admin.ModelAdmin):
    pass


admin.site.register(WorkoutPlan, WorkoutPlanAdmin)
admin.site.register(WorkoutExcercise, WorkoutExcerciseAdmin)
