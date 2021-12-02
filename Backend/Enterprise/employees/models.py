from django.db import models
from django.core.validators import int_list_validator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField


class Employee(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    employee_first_name = models.CharField(max_length=30)
    employee_last_name = models.CharField(max_length=30)
    employee_designation = models.CharField(max_length=30)
    employee_gender = models.CharField(max_length=10)
    employee_contact_number = PhoneNumberField()
    employee_manager_id = models.IntegerField()
    employee_email_id = models.EmailField(max_length=254)
    # project_list = ArrayField(ArrayField(models.IntegerField(max_length=10, blank=True), size=8, ), size=8, )
