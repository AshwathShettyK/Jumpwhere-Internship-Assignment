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


class Employee(TimeStampedModel):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'

    STATUS_CHOICES = [
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    designation = models.ForeignKey(
        'designations.Designation',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='employees',
    )
    projects = models.ManyToManyField(
        'projects.Project',
        through='EmployeeProject',
        blank=True,
        related_name='employees',
    )
    
    professional_summary = models.TextField(blank=True, help_text="Line-separated pointers")
    coding_skills = models.ManyToManyField('coding.Coding', blank=True, related_name='employees')
    tools = models.ManyToManyField('tools.Tool', blank=True, related_name='employees')
    
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=STATUS_ACTIVE)
    is_deleted = models.BooleanField(default=False)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='employee_created',
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='employee_updated',
    )

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['email'],
                condition=Q(is_deleted=False),
                name='unique_active_employee_email',
            ),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(update_fields=['is_deleted', 'updated_at'])


class EmployeeProject(TimeStampedModel):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='project_assignments',
    )
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name='employee_assignments',
    )
    role = models.CharField(max_length=100, blank=True)
    is_deleted = models.BooleanField(default=False)
    
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='employeeproject_created',
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='employeeproject_updated',
    )

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=['employee', 'project'],
                condition=Q(is_deleted=False),
                name='unique_active_employee_project',
            ),
        ]

    def __str__(self):
        return f"{self.employee} - {self.project}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save(update_fields=['is_deleted', 'updated_at'])
