from django.urls import path
from tasklist.api.views import (UserListCreateAPIView, UserDetailAPIView, 
                                CalendarListCreateAPIView, CalendarDetailAPIView, 
                                CalendarDayListCreateAPIView, CalendarDayDetailAPIView, 
                                CalendarEventListCreateAPIView, CalendarEventDetailAPIView, 
                                TaskListCreateAPIView, TaskListDetailAPIView, 
                                ListItemCreateAPIView, TaskListListAPIView)

urlpatterns = [
    path("users/", UserListCreateAPIView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name="user-detail"),

    path("users/<int:user_pk>/tasklist", TaskListCreateAPIView.as_view(), name="user-tasklist"),
    path("tasklists/", TaskListListAPIView.as_view(), name="tasklist-list"),
    path("tasklists/<int:pk>", TaskListDetailAPIView.as_view(), name="tasklists-detail"),

    path("tasklists/<int:tasklist_pk>/listitem", TaskListCreateAPIView.as_view(), name="tasklist-listitem"),

]