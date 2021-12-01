from django.urls import path
from .views import EmployeeViews, get_log_file

urlpatterns = [
    path('', EmployeeViews.as_view(), name="employee_names"),
    path('debug/', get_log_file, name="log_file"),
]
