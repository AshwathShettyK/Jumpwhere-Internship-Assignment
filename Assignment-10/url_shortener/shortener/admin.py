from django.contrib import admin
from .models import ShortenedUrl


@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ("short_code", "long_url", "click_count", "created_at")
    search_fields = ("short_code", "long_url")
    readonly_fields = ("created_at",)
