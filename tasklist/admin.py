from django.contrib import admin
from tasklist.models import  User, Calendar, CalendarDay, CalendarEvent, TaskList, ListItem

# Register your models here.

admin.site.register(User)
admin.site.register(Calendar)
admin.site.register(CalendarDay)
admin.site.register(CalendarEvent)
admin.site.register(TaskList)
admin.site.register(ListItem)