from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'status', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    search_fields = ('project_name', 'description')
    ordering = ('-created_at',)
