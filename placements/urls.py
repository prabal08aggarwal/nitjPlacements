from django.urls import path
from . import views as jobViews

urlpatterns = [
    path('',jobViews.index,name = 'jobPortal'), 
    path('apply/<int:idx>',jobViews.apply,name = 'apply'),
    path('applied',jobViews.applied,name = 'applied')
]

