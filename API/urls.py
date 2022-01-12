from django.urls import path

from .views import CarView

urlpatterns = [
    path('cars', CarView.as_view()),
]