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
   path('list/delete/<int:id>', views.delete_list, name="delete_list"),
   path('list/edit/<int:id>', views.edit_list, name="edit_list"),
   path('listitem/new/<int:id>', views.create_task, name="create_task"),
   path('listitem/delete/<int:item_id>/<int:list_id>', views.delete_task, name="delete_task"),
   path('listitem/edit/<int:item_id>/<int:list_id>', views.edit_task, name="delete_task"),
   path('api/day/<str:date>', views.api_one_day, name="one_day"),
   path('api/task/complete/<int:id>', views.api_complete_task, name="complete_task"),
   path('test', views.testroute, name="testroute"),
]