from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.CustomUserAPIView.as_view(), name = 'register'),
]