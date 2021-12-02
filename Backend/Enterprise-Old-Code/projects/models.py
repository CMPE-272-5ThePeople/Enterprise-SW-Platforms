# Create your models here.
from django.db import models
from django.core.validators import int_list_validator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=30)
    project_description = models.CharField(max_length=30)
    project_manager = models.CharField(max_length=30)
    project_start_date = models.DateField()

