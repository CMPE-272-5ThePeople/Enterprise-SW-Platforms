from rest_framework import serializers
from .models import APITest
from notifications.models import Notifications


class APITestSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(max_length=200)
    employee_designation = serializers.CharField(max_length=200)

    class Meta:
        model = APITest
        fields = '__all__'


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = '__all__'
