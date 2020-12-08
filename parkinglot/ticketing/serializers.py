from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'reg_no', 'color', 'allowed', 
        'createdAt')

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields: ("reg-no", "color", "allowed")