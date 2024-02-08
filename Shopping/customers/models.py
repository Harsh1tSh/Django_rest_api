from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length =256)
    age = models.IntegerField()
    address = models.CharField(max_length = 2000)
    phone_no = models.CharField(max_length = 8)
    