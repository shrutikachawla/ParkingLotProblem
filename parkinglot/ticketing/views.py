from django.shortcuts import render
from rest_framework import generics, status
from ticketing.serializers import CarSerializer, TicketSerializer
from ticketing.models import Car, Ticket
from rest_framework.views import APIView
from rest_framework.response import Response
import heapq
# Create your views here.

AVAILABLE_SLOTS = [11,12,13,14,15,16,17,18,19,10]
heapq.heapify(AVAILABLE_SLOTS)

class CarView(APIView):
    def get(self, request):
        model = Car.objects.all()
        serializer = CarSerializer(model, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(APIView):
    def get(self, request):
        regno = request.GET.get('regno')
        if regno is None:
            return Response("Registration no. can't be null", status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                model = Car.objects.get(regno=regno)
            except Car.DoesNotExist:
                return Response("Car not found", status = status.HTTP_404_NOT_FOUND)

            serializer = CarSerializer(model, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        regno = request.GET.get('regno')
        if regno is None:
            return Response("Registration no. can't be null", status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                model = Car.objects.get(regno= regno)
            except Car.DoesNotExist:
                return Response("Car not found", status = status.HTTP_404_NOT_FOUND)

            model.delete()
            return Response(status=status.HTTP_200_OK)


class Parking(APIView):

    def get(self,request):
        regno = request.GET.get('regno')
        if regno is None:
            return Response("Registration no. can't be null", status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                car = Car.objects.get(regno = regno)
            except Car.DoesNotExist:
                return Response("Car does not exist in our database", status = status.HTTP_404_NOT_FOUND)

            data = request.data
            data['carId'] = car.regno
            data['slotAllotted'] =  heapq.heappop(AVAILABLE_SLOTS)
            data['ticketNo'] = data['slotAllotted']
            serializer = TicketSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    