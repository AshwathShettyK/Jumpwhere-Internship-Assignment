from django.contrib import admin
from .models import SearchHistory


@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ("word", "searched_at")
    search_fields = ("word",)
    readonly_fields = ("searched_at",)
