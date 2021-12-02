from django.urls import path
from .views import EmployeeViews, NotificationViews

urlpatterns = [
    path('', EmployeeViews.as_view(), name="employee_names"),
    path('get_all_notifications/', NotificationViews.as_view(), name="notification_views"),
]
