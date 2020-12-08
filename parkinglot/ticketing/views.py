from django.shortcuts import render
from rest_framework import generics, status
from ticketing.serializers import ParkingSerializer, CarSerializer
from ticketing.models import Car
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


