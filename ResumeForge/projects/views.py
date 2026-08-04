from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import OperationalError, ProgrammingError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import ProjectForm
from .models import Project


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10

    def get_queryset(self):
        try:
            queryset = Project.objects.prefetch_related('coding_skills', 'tools').all()
        except (OperationalError, ProgrammingError):
            return Project.objects.none()

        search = self.request.GET.get('search', '').strip()
        status = self.request.GET.get('status', '').strip().lower()

        if search:
            queryset = queryset.filter(project_name__icontains=search)

        if status in [Project.STATUS_ACTIVE, Project.STATUS_CLOSED]:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '').strip()
        context['status_filter'] = self.request.GET.get('status', '').strip().lower()
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')

    def form_valid(self, form):
        project = form.save(commit=False)
        project.created_by = self.request.user
        project.updated_by = self.request.user
        project.save()
        form.save_m2m()  # Required to save many-to-many relationships when commit=False
        messages.success(self.request, 'Project created successfully.')
        return redirect(self.success_url)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('projects:list')

    def form_valid(self, form):
        project = form.save(commit=False)
        project.updated_by = self.request.user
        project.save()
        form.save_m2m()  # Required to save many-to-many relationships when commit=False
        messages.success(self.request, 'Project updated successfully.')
        return redirect(self.success_url)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'


class ProjectDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        project.is_deleted = True
        project.updated_by = request.user
        project.save(update_fields=['is_deleted', 'updated_by', 'updated_at'])
        messages.success(request, 'Project deleted successfully.')
        return redirect('projects:list')

    def get(self, request, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        return render(request, 'projects/delete_confirmation_modal.html', {'project': project})
