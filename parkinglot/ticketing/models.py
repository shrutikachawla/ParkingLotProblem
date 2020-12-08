from django.db import models
import uuid

# Create your models here.

#Cars in parking with slot in corresponding level
class Car(models.Model):
    regno = models.CharField(max_length=15, default=uuid.uuid1, primary_key=True)
    color = models.CharField(max_length=10, default='nocolor')
    status = models.CharField(max_length=3, default='in')
    slot = models.IntegerField(default=100)
    level = models.IntegerField(default=100)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    def __str__(self):
        return self.regno



class Ticket(models.Model):
    carId = models.ForeignKey(Car, on_delete=models.CASCADE,  null=False)
    slotAllotted = models.CharField(max_length=3, default=00)
    ticketNo = models.CharField(primary_key=True, max_length=3, default=uuid.uuid1)
    def __str__(self):
        return self.ticketNo

