from django.urls import path
from .views import CarView, CarDetail, Parking
#from .views import Parking

urlpatterns = [
    path('home/', CarView.as_view()),
    path('detail/', CarDetail.as_view(), name='car_list'),
    path('park/', Parking.as_view(), name="park_car")
    #path('park', TicketVi.as_view())
]