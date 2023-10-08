from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('chatbot/', views.chatbot, name='chatbot'),
]
