from django.contrib import admin

from .models import Designation


@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'designation_name', 'status', 'created_at', 'updated_at', 'is_deleted')
    list_filter = ('status', 'is_deleted')
    search_fields = ('designation_name', 'description')
    ordering = ('-created_at',)
