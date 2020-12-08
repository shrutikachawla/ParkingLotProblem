from django.urls import path
from .views import CarView
from .views import Parking

urlpatterns = [
    path('home', CarView.as_view()),
    path('park', Parking.as_view())
]