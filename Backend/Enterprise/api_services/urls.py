from django.urls import path
from .views import EmployeeViews, NotificationViews, TrainingViews, ProjectView

urlpatterns = [
    path('get_employee_details/', EmployeeViews.as_view(), name="employee_names"),
    path('get_all_notifications/', NotificationViews.as_view(), name="notification_views"),
    path('get_all_projects/', TrainingViews.as_view(), name="training_views"),
    path('get_all_trainings/', ProjectView.as_view(), name="project_views"),
]
