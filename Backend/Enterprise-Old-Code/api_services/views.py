from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeSerializer, NotificationsSerializer, TrainingSerializer, ProjectSerializer
from notifications.models import Notifications
from employees.models import Employee
from projects.models import Projects
from trainings.models import Training
from company_blog.models import Post


# Create your views here.
# @login_required
class EmployeeViews(APIView):
    def get(self, request):
        try:
            all_employee_objects = Employee.objects.all().values()
            api_response = {}

            for objects in all_employee_objects:
                api_response[objects['employee_id']] = {'employee_id': objects['employee_id'],
                                                        'employee_first_name': objects['employee_first_name'],
                                                        'employee_last_name': objects['employee_last_name'],
                                                        'employee_designation': objects['employee_designation'],
                                                        'employee_gender': objects['employee_gender'],
                                                        'employee_manager_id': objects['employee_manager_id'],
                                                        'employee_email_id': objects['employee_email_id']
                                                        }

            return Response({"status": "success",
                             "employee_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "employee_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "employee_data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                             "employee_data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class NotificationViews(APIView):
    def get(self, request):
        try:
            all_notifications_objects = Notifications.objects.all().values()
            api_response = {}
            for objects in all_notifications_objects:
                api_response[objects['id']] = {'message': objects['message'],
                                               'timestamp': objects['timestamp']}

            return Response({"status": "success",
                             "notification_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "notification_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = NotificationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "notification_data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                             "notification_data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class TrainingViews(APIView):
    def get(self, request):
        try:
            all_training_objects = Training.objects.all().values()
            api_response = {}
            for objects in all_training_objects:
                # TODO - Add here
                api_response[objects['id']] = {}

            return Response({"status": "success",
                             "training_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "training_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "training_data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                             "training_data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class ProjectView(APIView):
    def get(self, request):
        try:
            all_employee_objects = Projects.objects.all().values()
            api_response = {}

            for objects in all_employee_objects:
                # TODO - Add here
                api_response[objects['id']] = {}

            return Response({"status": "success",
                             "project_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "employee_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "project_data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error",
                             "project_data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class BlogViews(APIView):
    def get(self, request):
        try:
            all_post_objects = Post.objects.all().values()
            api_response = {}

            for objects in all_post_objects:
                # TODO ADD Data
                api_response[objects['id']] = {}

            return Response({"status": "success",
                             "blog_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "blog_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
