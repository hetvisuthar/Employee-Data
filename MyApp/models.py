from django.db import models
from django.utils.timezone import now

# Create your models here.

class employees(models.Model):
    employee_ID = models.IntegerField()
    employee_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_num = models.IntegerField()
