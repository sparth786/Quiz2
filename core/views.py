from rest_framework import viewsets
from core.serializers import (EmployeeSerializer,DepartmentSerializer)
from core.models import Employee, Department

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
