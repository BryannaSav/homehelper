from django.contrib import admin
from tasklist.models import User, CalendarEvent, TaskList, ListItem

admin.site.register(CalendarEvent)
admin.site.register(TaskList)
admin.site.register(ListItem)
