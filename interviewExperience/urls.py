from django.urls import path
from . import views as interview_views

urlpatterns = [
    path('',interview_views.index,name = 'interview'),
    path('newinterview', interview_views.newExpview, name='newInterview'),
    
]

