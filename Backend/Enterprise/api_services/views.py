from django.shortcuts import render
import json
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import APITestSerializer
from .models import APITest
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out


# Create your views here.
class EmployeeViews(APIView):
    @login_required
    def post(self, request):
        serializer = APITestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


def get_log_file(request):
    log_dict = []
    with open("debug.log", "r") as file:
        for index, line in enumerate(file):
            log_dict[index] = line
    return JsonResponse(log_dict, safe=False)
