from django.contrib import admin
from tasklist.models import  User, CalendarEvent, TaskList, ListItem

# Register your models here.

admin.site.register(User)
# admin.site.register(Calendar)
admin.site.register(CalendarEvent)
admin.site.register(TaskList)
admin.site.register(ListItem)