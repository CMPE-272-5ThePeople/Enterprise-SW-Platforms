from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import APITestSerializer, NotificationsSerializer
from notifications.models import Notifications
from .models import APITest
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out


# Create your views here.
class EmployeeViews(APIView):
    # @login_required
    def post(self, request):
        serializer = APITestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class NotificationViews(APIView):
    def get(self, request):
        all_notifications_objects = Notifications.objects.all().values()
        api_response = {}
        for objects in all_notifications_objects:
            api_response[objects['id']] = {'message': objects['message'],
                                           'timestamp': objects['timestamp']}

        return Response({"status": "success",
                         "notification_data": api_response},
                        status=status.HTTP_400_BAD_REQUEST)
