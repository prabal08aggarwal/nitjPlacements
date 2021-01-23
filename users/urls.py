from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('',auth_views.LoginView.as_view(template_name='users/index.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name = 'logout'),
]

