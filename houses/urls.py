from django.urls import path
from .views import HouseListCreateAPIView, HouseDetailAPIView

urlpatterns = [
    path('', HouseListCreateAPIView.as_view()),
    path('<int:pk>/', HouseDetailAPIView.as_view()),
]
