from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import EmployeeForm, EmployeeProjectForm
from .models import Employee, EmployeeProject


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        queryset = Employee.objects.select_related('designation').prefetch_related('coding_skills', 'tools').all()
        search = self.request.GET.get('search', '').strip()
        status = self.request.GET.get('status', '').strip().lower()

        if search:
            queryset = queryset.filter(
                models.Q(first_name__icontains=search) |
                models.Q(last_name__icontains=search) |
                models.Q(email__icontains=search) |
                models.Q(designation__designation_name__icontains=search)
            )

        if status in [Employee.STATUS_ACTIVE, Employee.STATUS_INACTIVE]:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '').strip()
        context['status_filter'] = self.request.GET.get('status', '').strip().lower()
        return context


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:list')

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.created_by = self.request.user
        employee.updated_by = self.request.user
        employee.save()
        form.save_m2m()  # Save many-to-many coding_skills and tools relationships
        messages.success(self.request, 'Employee created successfully.')
        return redirect(self.success_url)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:list')

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.updated_by = self.request.user
        employee.save()
        form.save_m2m()  # Save many-to-many coding_skills and tools relationships
        messages.success(self.request, 'Employee updated successfully.')
        return redirect(self.success_url)


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['assignments'] = self.object.project_assignments.filter(is_deleted=False).select_related('project')
        return context


class EmployeeProjectListView(LoginRequiredMixin, ListView):
    model = EmployeeProject
    template_name = 'employees/assignment_list.html'
    context_object_name = 'assignments'
    paginate_by = 10

    def get_queryset(self):
        queryset = EmployeeProject.objects.filter(is_deleted=False).select_related('employee', 'project')
        search = self.request.GET.get('search', '').strip()
        if search:
            queryset = queryset.filter(
                models.Q(employee__first_name__icontains=search) |
                models.Q(employee__last_name__icontains=search) |
                models.Q(project__project_name__icontains=search) |
                models.Q(role__icontains=search)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '').strip()
        return context


class EmployeeProjectCreateView(LoginRequiredMixin, CreateView):
    model = EmployeeProject
    form_class = EmployeeProjectForm
    template_name = 'employees/assignment_form.html'
    success_url = reverse_lazy('employees:assignments_list')

    def get_initial(self):
        initial = super().get_initial()
        employee_id = self.request.GET.get('employee')
        if employee_id:
            initial['employee'] = employee_id
        return initial

    def form_valid(self, form):
        assignment = form.save(commit=False)
        assignment.created_by = self.request.user
        assignment.updated_by = self.request.user
        assignment.save()
        messages.success(self.request, 'Project assignment created successfully.')
        return redirect(self.success_url)


class EmployeeProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = EmployeeProject
    form_class = EmployeeProjectForm
    template_name = 'employees/assignment_form.html'
    success_url = reverse_lazy('employees:assignments_list')

    def form_valid(self, form):
        assignment = form.save(commit=False)
        assignment.updated_by = self.request.user
        assignment.save()
        messages.success(self.request, 'Project assignment updated successfully.')
        return redirect(self.success_url)


class EmployeeProjectDetailView(LoginRequiredMixin, DetailView):
    model = EmployeeProject
    template_name = 'employees/assignment_detail.html'
    context_object_name = 'assignment'


class EmployeeProjectDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        assignment = get_object_or_404(EmployeeProject, pk=pk)
        assignment.is_deleted = True
        assignment.updated_by = request.user
        assignment.save(update_fields=['is_deleted', 'updated_by', 'updated_at'])
        messages.success(request, 'Project assignment deleted successfully.')
        return redirect('employees:assignments_list')

    def get(self, request, pk, *args, **kwargs):
        assignment = get_object_or_404(EmployeeProject, pk=pk)
        return render(request, 'employees/assignment_delete_confirmation.html', {'assignment': assignment})


class EmployeeDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=pk)
        employee.is_deleted = True
        employee.updated_by = request.user
        employee.save(update_fields=['is_deleted', 'updated_by', 'updated_at'])
        messages.success(request, 'Employee deleted successfully.')
        return redirect('employees:list')

    def get(self, request, pk, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=pk)
        return render(request, 'employees/delete_confirmation_modal.html', {'employee': employee})
