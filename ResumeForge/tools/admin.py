from django.contrib import admin

from .models import Tool


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id', 'tool_name', 'status', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    search_fields = ('tool_name', 'description')
    ordering = ('-created_at',)
