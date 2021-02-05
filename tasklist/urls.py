from django.urls import path
from . import views

urlpatterns = [
   path('', views.register, name='register'),
   path('login', views.user_login, name="login"),
   path('logout', views.user_logout, name="logout"),
   path('dashboard', views.dashboard, name="dashboard"),
   path('lists', views.lists, name="lists"),
   path('list/new', views.create_list, name="create_list"),
   path('list/<int:id>', views.one_list, name="one_list"),
   path('listitem/new/<int:id>', views.create_task, name="create_task"),
   path('api/day/<str:date>', views.api_one_day, name="one_day"),
   path('api/task/complete/<int:id>', views.api_complete_task, name="complete_task"),
   path('test', views.testroute, name="testroute"),
]