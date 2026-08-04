from django.contrib import admin

from .models import Coding


@admin.register(Coding)
class CodingAdmin(admin.ModelAdmin):
    list_display = ('id', 'coding_name', 'status', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    search_fields = ('coding_name', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
