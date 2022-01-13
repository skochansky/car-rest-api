from django.urls import path

from .views import CarView, CarDeleteView

urlpatterns = [
    path('cars', CarView.as_view()),
    path('cars/<int:car_id>', CarDeleteView.as_view()),
]