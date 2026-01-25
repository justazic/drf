from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UsersListAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('list/', UsersListAPIView.as_view(), name='list'),
]