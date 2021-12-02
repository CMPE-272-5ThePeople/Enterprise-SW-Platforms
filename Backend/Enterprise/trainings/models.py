# Create your models here.
from django.db import models
from django.core.validators import int_list_validator
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Training(models.Model):
    training_id = models.IntegerField(primary_key=True)
    training_name = models.CharField(max_length=30)
    training_description = models.CharField(max_length=256)
    training_total_hours = models.IntegerField()
