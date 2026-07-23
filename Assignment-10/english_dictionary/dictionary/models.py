from django.db import models
from django.utils import timezone


class SearchHistory(models.Model):
    word = models.CharField(max_length=100)
    searched_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-searched_at"]

    def __str__(self):
        return f"{self.word} searched at {self.searched_at:%Y-%m-%d %H:%M:%S}"
