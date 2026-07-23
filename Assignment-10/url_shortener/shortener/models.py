from django.db import models
from django.utils import timezone
import random
import string


def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


class ShortenedUrl(models.Model):
    long_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=12, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    click_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
            while ShortenedUrl.objects.filter(short_code=self.short_code).exists():
                self.short_code = generate_short_code()
        super().save(*args, **kwargs)
