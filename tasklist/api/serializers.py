from rest_framework import serializers
from tasklist.models import  User, Calendar, CalendarDay, CalendarEvent, TaskList, ListItem


class CalendarEventSerializer(serializers.ModelSerializer):

    class Meta:
        model = CalendarEvent
        fields = "__all__"


class CalendarDaySerializer(serializers.ModelSerializer):
    calendar_events = CalendarEventSerializer(many=True)

    class Meta:
        model = CalendarDay
        fields = "__all__"


class CalendarSerializer(serializers.ModelSerializer):
    days = CalendarDaySerializer(many=True, read_only=True)

    class Meta:
        model = Calendar
        fields = "__all__"


class ListItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListItem
        fields = "__all__"


class TaskListSerializer(serializers.ModelSerializer):
    #list_items = ListItemSerializer(many=True)

    class Meta:
        model = TaskList
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    # For testing, may remove later depending on needed api calls
    task_lists = TaskListSerializer(many=True)
    calendars = CalendarSerializer(many=True)

    class Meta:
        model = User
        fields = "__all__"
