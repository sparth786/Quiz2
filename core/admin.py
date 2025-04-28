from django.contrib import admin
from core.models import Attendance, Employee, Department, Performance


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'designation', 'salary', 'join_date')
    search_fields = ('name', 'email', 'designation')
    list_filter = ('department', 'join_date')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'review_date', 'rating')
    list_filter = ('rating', 'review_date')

    
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date', 'status')
    list_filter = ('status', 'date')
