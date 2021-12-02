from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from employee.models import Employee, Department, Role, Leave
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out


# Create your views here.
class EmployeeViews(APIView):
    def get(self, request):
        try:
            all_employee_objects = Employee.objects.all().values()
            api_response = {}

            for objects in all_employee_objects:
                api_response[objects['id']] = {
                    'image': objects['image'],
                    'firstname': objects['firstname'],
                    'lastname': objects['lastname'],
                    'othername': objects['othername'],
                    'birthday': objects['birthday'],
                    'role_id': objects['role_id'],
                    'startdate': objects['startdate'],
                    'employeetype': objects['employeetype'],
                    'employeeid': objects['employeeid'],
                    'dateissued': objects['dateissued'],
                    'is_blocked': objects['is_blocked'],
                    'is_deleted': objects['is_deleted'],
                    'created': objects['created'],
                    'updated': objects['updated']
                }
            return Response({"status": "success",
                             "employee_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "employee_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
class DepartmentViews(APIView):
    def get(self, request):
        try:
            all_department_objects = Department.objects.all().values()
            api_response = {}

            for objects in all_department_objects:
                api_response[objects['id']] = {
                    'name': objects['name'],
                    'description': objects['description'],
                    'created': objects['created'],
                    'updated': objects['updated']
                }
            return Response({"status": "success",
                             "department_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "department_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class RoleViews(APIView):
    def get(self, request):
        try:
            all_role_objects = Role.objects.all().values()
            api_response = {}

            for objects in all_role_objects:
                api_response[objects['id']] = {
                    'name': objects['name'],
                    'description': objects['description'],
                    'created': objects['created'],
                    'updated': objects['updated']
                }
            return Response({"status": "success",
                             "role_data": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "role_data": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)


class LeaveViews(APIView):
    def get(self, request):
        try:
            all_leave_objects = Leave.objects.all().values()
            api_response = {}

            for objects in all_leave_objects:
                print(objects)
                api_response[objects['id']] = {
                    'user_id': objects['user_id'],
                    'startdate': objects['startdate'],
                    'enddate': objects['enddate'],
                    'leavetype': objects['leavetype'],
                    'reason': objects['reason'],
                    'defaultdays': objects['defaultdays'],
                    'status': objects['status'],
                    'is_approved': objects['is_approved'],
                    'updated': objects['updated'],
                    'created': objects['created'],
                }
            return Response({"status": "success",
                             "leave_details": api_response},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error",
                             "leave_details": str(e)},
                            status=status.HTTP_400_BAD_REQUEST)
