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
   path('test', views.testroute, name="testroute"),
]