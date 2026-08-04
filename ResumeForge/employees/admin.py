from django.contrib import admin

from .models import Employee, EmployeeProject


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'designation', 'status', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'designation__designation_name')
    ordering = ('-created_at',)


@admin.register(EmployeeProject)
class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'project', 'role', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('is_deleted',)
    search_fields = ('employee__first_name', 'employee__last_name', 'project__project_name', 'role')
    ordering = ('-created_at',)
