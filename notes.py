

for wd in WeekDay.objects.all():
    print(wd.get_day_display(), wd.day)
