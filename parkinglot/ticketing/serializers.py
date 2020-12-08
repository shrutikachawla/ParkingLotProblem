from rest_framework import serializers
from .models import Car, Ticket

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

class DynamicCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['regno']

class CarSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['slot']