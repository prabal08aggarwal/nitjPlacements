from django.urls import path
from . import views as interview_views

urlpatterns = [
    path('',interview_views.index,name = 'interview')
]

