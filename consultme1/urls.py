from django.urls import path
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from chatme.views import *

urlpatterns = [
     path('register/', RegisterView.as_view(), name='auth_register'),
     path('api-token-auth/', CustomAuthToken.as_view()),
     path('lawyer/', lawyerList.as_view()),
     path('lawyer/<int:pk>/', lawyerDetail.as_view()),  
     path('client/', clientList.as_view()),
     path('client/<int:pk>/', clientDetail.as_view()),
     path('chat/<str:room_name>/', ChatView, name='chat'),
     path('meff/<int:pk>/', userffDetail.as_view()),
     path('information/',infoList.as_view()),
     path('lawfirm/', lawfirmList.as_view()),
     path('lawfirm/<int:pk>/', lawfirmDetail.as_view()),
     path('verified/', verifiedList.as_view()),
     path('verified/<int:pk>/', verifiedDetail.as_view()),
     path('rating/', rartingList.as_view()),
     path('rating/<int:pk>/', rartingDetail.as_view()),
     path('profilepic/', profileList.as_view()),
     path('profileDetail/', profileDetail.as_view()),
     path('active/', activeList.as_view()),
     path('active/<int:pk>/', activeDetail.as_view()),
     
    
]