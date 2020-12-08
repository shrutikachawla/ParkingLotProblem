from django.db import models

# Create your models here.
class Car(models.Model):
    reg_no = models.CharField(max_length=14, default="")
    color = models.CharField(max_length = 10)
    allowed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reg_no

