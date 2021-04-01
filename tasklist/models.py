from django.db import models
from django.contrib.auth.models import User 
from django.forms import ModelForm

class CalendarEvent(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
                    User, 
                    on_delete=models.CASCADE, 
                    related_name="calendar_events")

    def __str__(self):
        return self.name

class CalendarEventForm(ModelForm):
    class Meta: 
        model = CalendarEvent
        fields = ['name', 'start_date']

class TaskList(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
                    User, 
                    on_delete=models.CASCADE, 
                    related_name="task_lists")

    def __str__(self):
        return self.name
 
class TaskListForm(ModelForm):
    class Meta: 
        model = TaskList
        fields = ['name', 'description']
        
class ListItem(models.Model):
    task = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    user = models.ForeignKey(
                    User, 
                    on_delete=models.CASCADE, 
                    related_name="list_items")

    def __str__(self):
        return self.task

class ListItemForm(ModelForm):
    class Meta: 
        model = ListItem
        fields = ['task', 'due_date']
        