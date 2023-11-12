from django.urls import path
from . views import create_user
from django.contrib.auth import views

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('log-in/', views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
]
