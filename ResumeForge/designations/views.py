from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import OperationalError, ProgrammingError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import DesignationForm
from .models import Designation


class DesignationListView(LoginRequiredMixin, ListView):
    model = Designation
    template_name = 'designations/designation_list.html'
    context_object_name = 'designations'
    paginate_by = 10

    def get_queryset(self):
        try:
            queryset = Designation.objects.all()
        except (OperationalError, ProgrammingError):
            return Designation.objects.none()

        search = self.request.GET.get('search', '').strip()
        status = self.request.GET.get('status', '').strip().lower()

        if search:
            queryset = queryset.filter(designation_name__icontains=search)

        if status in [Designation.STATUS_ACTIVE, Designation.STATUS_INACTIVE]:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '').strip()
        context['status_filter'] = self.request.GET.get('status', '').strip().lower()
        return context


class DesignationCreateView(LoginRequiredMixin, CreateView):
    model = Designation
    form_class = DesignationForm
    template_name = 'designations/designation_form.html'
    success_url = reverse_lazy('designations:list')

    def form_valid(self, form):
        designation = form.save(commit=False)
        designation.created_by = self.request.user
        designation.updated_by = self.request.user
        designation.save()
        messages.success(self.request, 'Designation created successfully.')
        return redirect(self.success_url)


class DesignationUpdateView(LoginRequiredMixin, UpdateView):
    model = Designation
    form_class = DesignationForm
    template_name = 'designations/designation_form.html'
    success_url = reverse_lazy('designations:list')

    def form_valid(self, form):
        designation = form.save(commit=False)
        designation.updated_by = self.request.user
        designation.save()
        messages.success(self.request, 'Designation updated successfully.')
        return redirect(self.success_url)


class DesignationDetailView(LoginRequiredMixin, DetailView):
    model = Designation
    template_name = 'designations/designation_detail.html'
    context_object_name = 'designation'


class DesignationDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        designation = get_object_or_404(Designation, pk=pk)
        designation.is_deleted = True
        designation.updated_by = request.user
        designation.save(update_fields=['is_deleted', 'updated_by', 'updated_at'])
        messages.success(request, 'Designation deleted successfully.')
        return redirect('designations:list')

    def get(self, request, pk, *args, **kwargs):
        designation = get_object_or_404(Designation, pk=pk)
        return render(request, 'designations/delete_confirmation_modal.html', {'designation': designation})
