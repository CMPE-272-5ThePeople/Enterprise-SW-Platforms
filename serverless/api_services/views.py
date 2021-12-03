import os

from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import os


class SendMail(APIView):
    def post(self, request):
        try:
            send_mail('Testing Mail',
                      'This is a testing message',
                      'shreya.nimbhorkar@gmail.com',
                      ['aryanjadon94@gmail.com'])

            return Response({"status": "success"},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "success"},
                            status=status.HTTP_200_OK)
