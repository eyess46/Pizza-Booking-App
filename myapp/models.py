from django.db import models


# Create your models here.


class Order(models.Model):
    name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20)
    date_needed = models.DateField()
    email = models.EmailField()
    address = models.CharField(max_length=10000)
    request = models.CharField(max_length=100000)
    payment_reciept = models.ImageField(upload_to='payment_slip/')
