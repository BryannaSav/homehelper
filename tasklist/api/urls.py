from django.urls import path
from tasklist.api.views import (UserListCreateAPIView, UserDetailAPIView, 
                                CalendarListCreateAPIView, CalendarDetailAPIView, 
                                CalendarDayListCreateAPIView, CalendarDayDetailAPIView, 
                                CalendarEventListCreateAPIView, CalendarEventDetailAPIView, 
                                TaskListListCreateAPIView, TaskListDetailAPIView, 
                                ListItemCreateAPIView)



urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),

    path("calendars/", CalendarListCreateAPIView.as_view(), name="calendar-list"),
    path("calendars/<int:pk>/", CalendarDetailAPIView.as_view(), name="calendar-detail"),

    path("tasklists/", TaskListListCreateAPIView.as_view(), name="tasklist-list"),
    path("tasklists/<int:pk>", TaskListDetailAPIView.as_view(), name="tasklists-detail"),


]