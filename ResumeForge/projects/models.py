from django.conf import settings
from django.db import models
from django.db.models import Q


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(is_deleted=True)

    def hard_delete(self):
        return super().delete()

    def alive(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(is_deleted=False)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(TimeStampedModel):
    STATUS_ACTIVE = 'active'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_CLOSED, 'Closed'),
    ]

    project_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    role_responsibilities = models.TextField(blank=True, help_text="Line-separated pointers")
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    is_deleted = models.BooleanField(default=False)
    
    coding_skills = models.ManyToManyField('coding.Coding', blank=True, related_name='projects')
    tools = models.ManyToManyField('tools.Tool', blank=True, related_name='projects')

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='project_created',
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='project_updated',
    )

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['project_name'],
                condition=Q(is_deleted=False),
                name='unique_active_project_name',
            ),
        ]

    def __str__(self):
        return self.project_name

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(update_fields=['is_deleted', 'updated_at'])
