from django.urls import path
from .views import CarView

urlpatterns = [
    path('home', CarView.as_view())
]