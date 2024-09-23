from django.contrib import admin
from .models import Employee, Role, department, Carausel
# Register your models here.

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(department)
admin.site.register(Carausel)