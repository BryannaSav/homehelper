from rest_framework import generics, status

from tasklist.models import (User, Calendar, CalendarDay, 
                                        CalendarEvent, TaskList, ListItem)
from tasklist.api.serializers import (UserSerializer, CalendarEventSerializer, 
                                        CalendarSerializer, CalendarDaySerializer, 
                                        TaskListSerializer, ListItemSerializer)
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

#-------------------- USER -------------------#

class UserListCreateAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class UserDetailAPIView(APIView):

    def get_object(self, pk):
        user = get_object_or_404(User, pk=pk)
        return user

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------- CALENDAR -------------------#
    
class CalendarListCreateAPIView(APIView):

    def get(self, request):
        calendars = Calendar.objects.all()
        serializer = CalendarSerializer(calendars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class CalendarDetailAPIView(APIView):

    def get_object(self, pk):
        calendar = get_object_or_404(Calendar, pk=pk)
        return calendar

    def get(self, request, pk):
        calendar = self.get_object(pk)
        serializer = CalendarSerializer(calendar)
        return Response(serializer.data)

    def put(self, request, pk):
        calendar = self.get_object(pk)
        serializer = CalendarSerializer(calendar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        calendar = self.get_object(pk)
        calendar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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

class TaskListListCreateAPIView(APIView):

    def get(self, request):
        tasklists = TaskList.objects.all()
        serializer = TaskListSerializer(tasklists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class TaskListDetailAPIView(APIView):

    def get_object(self, pk):
        tasklist = get_object_or_404(TaskList, pk=pk)
        return tasklist

    def get(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer(tasklist)
        return Response(serializer.data)

    def put(self, request, pk):
        tasklist = self.get_object(pk)
        serializer = TaskListSerializer(tasklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tasklist = self.get_object(pk)
        tasklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------- LIST ITEM -------------------#

class ListItemCreateAPIView(generics.CreateAPIView):
    queryset = ListItem.objects.all()
    serializer_class = ListItemSerializer

    def perform_create(self, serializer):
        tasklist_pk = self.kwargs.get("tasklist_pk")
        tasklist = get_object_or_404(TaskList, pk=tasklist_pk)
        serializer.save(tasklist=tasklist)


