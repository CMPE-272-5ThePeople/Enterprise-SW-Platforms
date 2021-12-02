from django.contrib import admin
from employee.models import Role,Department,Employee, Project, Training



admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Training)
