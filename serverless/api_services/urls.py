from django.urls import path
from .views import SendMail

urlpatterns = [
    path('sendmail/', SendMail.as_view(), name="send_mail"),
]
