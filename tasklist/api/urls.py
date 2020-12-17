from django.urls import path
from tasklist.api.views import (UserListCreateAPIView, UserDetailAPIView, 
                                CalendarListCreateAPIView, CalendarDetailAPIView, 
                                CalendarDayListCreateAPIView, CalendarDayDetailAPIView, 
                                CalendarEventListCreateAPIView, CalendarEventDetailAPIView, 
                                TaskListListCreateAPIView, TaskListDetailAPIView, 
                                ListItemListCreateAPIView, ListItemDetailAPIView)



urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),

    path("calendars/", CalendarListCreateAPIView.as_view(), name="calendar-list"),
    path("calendars/<int:pk>/", CalendarDetailAPIView.as_view(), name="calendar-detail"),

    path("calendardays/", CalendarDayListCreateAPIView.as_view(), name="calendarday-list"),
    path("calendardays/<int:pk>/", CalendarDayDetailAPIView.as_view(), name="calendarday-detail"),
    
    path("calendarevents/", CalendarEventListCreateAPIView.as_view(), name="calendarevent-list"),
    path("calendarevents/<int:pk>/", CalendarEventDetailAPIView.as_view(), name="calendarevent-detail"),

    path("tasklists/", TaskListListCreateAPIView.as_view(), name="tasklist-list"),
    path("tasklists/<int:pk>", TaskListDetailAPIView.as_view(), name="tasklist-detail"),

    path("listitems/", ListItemListCreateAPIView.as_view(), name="listitem-list"),
    path("listitems/<int:pk>", ListItemDetailAPIView.as_view(), name="listitem-detail"),


]