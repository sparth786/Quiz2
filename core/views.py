from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny

from core.serializers import (EmployeeSerializer,DepartmentSerializer, AttendanceSerializer, PerformanceSerializer)
from core.models import Employee, Department, Attendance, Performance

from django.db.models import Avg
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['department', 'designation']
    search_fields = ['name', 'email']
    ordering_fields = ['salary', 'join_date']

    @action(detail=False, methods=['get'])
    def average_salary(self, request):
        salary_stats = Employee.objects.aggregate(average_salary=Avg('salary'))
        return Response({"average_salary": salary_stats['average_salary']})


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location']
    search_fields = ['name']


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'date', 'status']
    search_fields = ['status']


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'review_date']
    search_fields = ['comments']
    ordering_fields = ['rating', 'review_date']


class EmployeePerformanceSummary(APIView):
    """
    Returns a performance summary for chart visualization.
    """
    permission_classes = [AllowAny]

    def get(self, request):
        all_performance_records = Performance.objects.all()
        summary_data = {
            'labels': [f"{record.employee.name}" for record in all_performance_records],
            'performance_scores': [record.rating for record in all_performance_records]
        }
        return Response(summary_data)



class EmployeePerformanceSummaryChart(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return render(request, 'data_chart/emp_performance_chart.html')
