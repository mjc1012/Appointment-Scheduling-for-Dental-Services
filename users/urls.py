from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('register/',views.register, name='register'),
    path('update_user_info/<int:pk>/', views.update_user, name='update_user_info'),
    path('password/', Password_Change_View.as_view(template_name='registration/change-password.html'), name="password"),
    path('delete_user/<int:pk>/',
         Delete_User_View.as_view(), name='delete_user'),
]
