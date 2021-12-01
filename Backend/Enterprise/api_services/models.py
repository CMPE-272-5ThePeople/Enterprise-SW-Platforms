from django.db import models


# Create your models here.

class APITest(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_designation = models.CharField(max_length=200)
