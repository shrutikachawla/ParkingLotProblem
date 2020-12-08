from django.shortcuts import render
from rest_framework import generics, status
from ticketing.serializers import CarSerializer, TicketSerializer, DynamicCarSerializer, CarSlotSerializer
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


class TicketView(APIView):
    def get(self, request):
        model = Ticket.objects.all()
        serializer = TicketSerializer(model, many = True)
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
                model = Car.objects.get(pk=regno)
            except Car.DoesNotExist:
                return Response("Car not found", status = status.HTTP_404_NOT_FOUND)

            serializer = CarSerializer(model)
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

            if car.slot!=100:
                return Response("Car is already parked", status = status.HTTP_208_ALREADY_REPORTED)

            data = request.data
            data['carId'] = car.regno
            data['slotAllotted'] =  heapq.heappop(AVAILABLE_SLOTS)
            data_car = request.data
            data_car['level'] = int(str(data['slotAllotted'])[0])
            data_car['slot'] = int(str(data['slotAllotted'])[1])
            serializer = TicketSerializer(data=data)
            car_serializer = CarSerializer(car, data=data_car)
            if serializer.is_valid():
                if car_serializer.is_valid():
                    serializer.save()
                    car_serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Leave(APIView):
    def get(self, request):
        ticketNo = request.GET.get('ticketNo')
        if ticketNo is None:
            return Response("Ticket no. can't be null", status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                ticket = Ticket.objects.get(ticketNo = ticketNo)
            except Ticket.DoesNotExist:
                return Response("OOPS! This ticket has not been issued from our system", status = status.HTTP_404_NOT_FOUND)

            if ticket.slotAllotted=='00':
                return Response("You have already taken you vehicle from our space", status=status.HTTP_404_NOT_FOUND)

            data = request.data
            heapq.heappush(AVAILABLE_SLOTS, int(ticket.slotAllotted))
            data['slotAllotted'] =  '00'
            data['carId'] = ticket.carId
            
            car = Car.objects.get(regno=ticket.carId)
            data_car = request.data
            data_car['level'] = 100
            data_car['slot'] = 100
            serializer = TicketSerializer(ticket, data=data)
            car_serializer = CarSerializer(car, data=data_car)
            if serializer.is_valid():
                if car_serializer.is_valid():
                    serializer.save()
                    car_serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegNoByColor(APIView):

    def get(self, request):
        color = request.GET.get('color')
        if color is None:
            return Response("Color can't be null", status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                cars = Car.objects.filter(color__exact=color).values('regno')
            except Car.DoesNotExist:
                return Response("OOPS! We don't have any car in this color", status = status.HTTP_404_NOT_FOUND)

        serializer = DynamicCarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)

class SlotByReg(APIView):

    def get(self, request):    
        regno = request.GET.get('regno')
        if regno is None:
            return Response("Registration no. can't be null", status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                cars = Car.objects.filter(regno=regno).values('slot')
            
            except Car.DoesNotExist:
                return Response("Car not found", status = status.HTTP_404_NOT_FOUND)

        serializer = CarSlotSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
