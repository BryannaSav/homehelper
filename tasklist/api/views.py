from rest_framework import generics, status

from tasklist.models import (User, CalendarEvent, TaskList, ListItem)
from tasklist.api.serializers import (UserSerializer, CalendarEventSerializer, 
                                        # CalendarSerializer, CalendarDaySerializer, 
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
    
# class CalendarListCreateAPIView(APIView):

#     def get(self, request):
#         calendars = Calendar.objects.all()
#         serializer = CalendarSerializer(calendars, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CalendarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# class CalendarDetailAPIView(APIView):

#     def get_object(self, pk):
#         calendar = get_object_or_404(Calendar, pk=pk)
#         return calendar

#     def get(self, request, pk):
#         calendar = self.get_object(pk)
#         serializer = CalendarSerializer(calendar)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         calendar = self.get_object(pk)
#         serializer = CalendarSerializer(calendar, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         calendar = self.get_object(pk)
#         calendar.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#-------------------- CALENDAR DAY -------------------#

# class CalendarDayListCreateAPIView(APIView):

#     def get(self, request):
#         print("Getting calendar day")
#         calendardays = CalendarDay.objects.all()
#         serializer = CalendarDaySerializer(calendardays, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         print("Hitting calendar day post route")
#         serializer = CalendarDaySerializer(data=request.data)
#         if serializer.is_valid():
#             print("Saving calendar day")
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print("Error on saving calendar day")
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class CalendarDayDetailAPIView(APIView):

#     def get_object(self, pk):
#         calendarday = get_object_or_404(CalendarDay, pk=pk)
#         return calendarday

#     def get(self, request, pk):
#         calendarday = self.get_object(pk)
#         serializer = CalendarDaySerializer(calendarday)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         calendarday = self.get_object(pk)
#         serializer = CalendarDaySerializer(calendarday, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         calendarday = self.get_object(pk)
#         calendarday.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------- CALENDAR EVENT -------------------#

class CalendarEventListCreateAPIView(APIView):

    def get(self, request):
        calendarevents = CalendarEvent.objects.all()
        serializer = CalendarEventSerializer(calendarevents, many=True)
        return Response(serializer.data)

    def post(self, request):
        # NEED TO FIX SO IT DOESN'T NEED BOTH A START DATE AND DAY RELATIONSHIP
        # What to do about end date?  Add to multiple days?
        serializer = CalendarEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CalendarEventDetailAPIView(APIView):

    def get_object(self, pk):
        calendarevent = get_object_or_404(CalendarEvent, pk=pk)
        return calendarevent

    def get(self, request, pk):
        calendarevent = self.get_object(pk)
        serializer = CalendarEventSerializer(calendarevent)
        return Response(serializer.data)

    def put(self, request, pk):
        calendarevent = self.get_object(pk)
        serializer = CalendarEventSerializer(calendarevent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        calendarevent = self.get_object(pk)
        calendarevent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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

class ListItemListCreateAPIView(APIView):

    def get(self, request):
        listitems = ListItem.objects.all()
        serializer = ListItemSerializer(listitems, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class ListItemDetailAPIView(APIView):

    def get_object(self, pk):
        listitem = get_object_or_404(ListItem, pk=pk)
        return listitem

    def get(self, request, pk):
        listitem = self.get_object(pk)
        serializer = ListItemSerializer(listitem)
        return Response(serializer.data)

    def put(self, request, pk):
        listitem = self.get_object(pk)
        serializer = ListItemSerializer(listitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        listitem = self.get_object(pk)
        listitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



