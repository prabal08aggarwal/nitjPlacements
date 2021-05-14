from django.urls import path
from . import views as user_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',user_views.register,name = 'register'),
    path('',auth_views.LoginView.as_view(template_name='users/index.html'),name = 'homePage'), #Login view
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name = 'logout'),
    path('resume/<username>/',user_views.viewResume,name = 'resume'),
    
    #Authenticated views
    path('profile/',user_views.profile,name = 'profile')
]

