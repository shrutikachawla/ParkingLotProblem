from django.shortcuts import render
from rest_framework import generics, status
from .serializers import CarSerializer, ParkingSerializer
from .models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class CarView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class Parking(APIView):
    serializer_class = ParkingSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            reg_no = serializer.data.reg_no
            color = serializer.data.color
            car = Car(reg_no, color)
            car.save()

            return Response(CarSerializer(car).data, status=status.HTTP_202_ACCEPTED)
            