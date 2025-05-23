from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from core.views import EmployeeViewSet, DepartmentViewSet, AttendanceViewSet, PerformanceViewSet, EmployeePerformanceSummary, EmployeePerformanceSummaryChart


# DRF Router
router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'attendance', AttendanceViewSet, basename='attendance')
router.register(r'performance', PerformanceViewSet, basename='performance')


schema_view = get_schema_view(
    openapi.Info(
        title="Employee Dashboard API",
        default_version='v1',
        description="API for employee analytics and visualizations",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="admin@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=()
)

# URL Patterns
urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', obtain_auth_token),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('performance-summary/', EmployeePerformanceSummary.as_view(), name='performance_summary'),
    path('performance-chart/', EmployeePerformanceSummaryChart.as_view(), name='performance-chart'),
]
