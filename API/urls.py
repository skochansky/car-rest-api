from django.urls import path

from .views import CarView, CarDeleteView, CarRatingView, CarPopularityView

urlpatterns = [
    path("cars/", CarView.as_view()),
    path("cars/<int:car_id>", CarDeleteView.as_view()),
    path("rate/", CarRatingView.as_view()),
    path("popular/", CarPopularityView.as_view()),
]
