from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='qAindex'),
    path('new-question', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='questionPage'),
    #path('reply', views.replyPage, name='reply')
]
