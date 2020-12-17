from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Calendar(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calendars")

    def __str__(self):
        return self.name
        

class CalendarDay(models.Model):
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    day = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    day_name = models.CharField(max_length=8)
    month_name = models.CharField(max_length=9)
    holiday_flag = models.BooleanField(default=False)
    weekend_flag = models.BooleanField(default=False)

    calendar = models.ManyToManyField(Calendar)

    def __str__(self):
        return self.day_name + " " + self.month_name + " " + str(self.day)


class CalendarEvent(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    day = models.ForeignKey(CalendarDay, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TaskList(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_lists")

    def __str__(self):
        return self.name
        

class ListItem(models.Model):
    task = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    day = models.ForeignKey(CalendarDay, on_delete=models.CASCADE)

    def __str__(self):
        return self.task