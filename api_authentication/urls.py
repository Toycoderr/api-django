from django.urls import path, include
from .views import Register, LoginView, UserView, LogoutView


urlpatterns = [
    path('register', Register.as_view(), name='Register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('user', UserView.as_view(), name='user')
]