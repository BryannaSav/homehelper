from rest_framework import generics, status

from tasklist.models import  User, Calendar, CalendarDay, CalendarEvent, TaskList, ListItem
from tasklist.api.serializers import  (UserSerializer, CalendarSerializer, CalendarDaySerializer, 
                                        CalendarEventSerializer, TaskListSerializer, ListItemSerializer)
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

#-------------------- USER -------------------#

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#-------------------- CALENDAR -------------------#
    
class CalendarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer


class CalendarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

#-------------------- CALENDAR DAY -------------------#

class CalendarDayListCreateAPIView(generics.ListCreateAPIView):
    queryset = CalendarDay.objects.all()
    serializer_class = CalendarDaySerializer


class CalendarDayDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalendarDay.objects.all()
    serializer_class = CalendarDaySerializer

#-------------------- CALENDAR EVENT -------------------#

class CalendarEventListCreateAPIView(generics.ListCreateAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer


class CalendarEventDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer

#-------------------- TASK LIST -------------------#

class TaskListCreateAPIView(generics.CreateAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def perform_create(self, serializer):
        # Currently creates task list but does not add user to it
        user_pk = self.kwargs.get("user_pk")
        user = get_object_or_404(User, pk=user_pk) 


class TaskListListAPIView(generics.ListAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskListDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

#-------------------- LIST ITEM -------------------#

class ListItemCreateAPIView(generics.CreateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def perform_create(self, serializer):
        tasklist_pk = self.kwargs.get("tasklist_pk")
        tasklist = get_object_or_404(TaskList, pk=tasklist_pk)
        serializer.save(tasklist=tasklist)


