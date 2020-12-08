from django.db import models

# Create your models here.

#Cars in parking with slot in corresponding level
class Car(models.Model):
    regno = models.CharField(max_length=15, default="XXXXXXXX")
    color = models.CharField(max_length=10, default='nocolor')
    status = models.CharField(max_length=3, default='in')
    slot = models.IntegerField(default=999)
    level = models.IntegerField(default=999)
    def __str__(self):
        return self.regno


#Multi-storey parking lot
class Parking(models.Model):
    level = models.CharField(max_length=200, unique=True)
    slot1 = models.IntegerField(default=0)
    slot2 = models.IntegerField(default=0)
    slot3 = models.IntegerField(default=0)
    slot4 = models.IntegerField(default=0)
    slot5 = models.IntegerField(default=0)
    slot6 = models.IntegerField(default=0)
    slot7 = models.IntegerField(default=0)
    slot8 = models.IntegerField(default=0)
    slot9 = models.IntegerField(default=0)
    slot10 = models.IntegerField(default=0)
    def __str_(self):
        return self.level
