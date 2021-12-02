from django.urls import path
from .views import EmployeeViews, DepartmentViews, RoleViews, LeaveViews

app_name = 'api_services'

urlpatterns = [
    path('get_employee_details/', EmployeeViews.as_view(), name="employee_names"),
    path('get_department_details/', DepartmentViews.as_view(), name="department_names"),
    path('get_role_details/', RoleViews.as_view(), name="role_names"),
    path('get_leave_details/', LeaveViews.as_view(), name="leave_details"),
]
