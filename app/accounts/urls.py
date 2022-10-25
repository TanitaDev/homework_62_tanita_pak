from django.contrib import admin
from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, DeleteUser
from webapp.views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/delete', DeleteUser.as_view(), name='delete_user')
]
