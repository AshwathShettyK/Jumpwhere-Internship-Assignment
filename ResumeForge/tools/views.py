from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View

from .forms import ToolForm
from .models import Tool


class ToolListView(LoginRequiredMixin, ListView):
    model = Tool
    template_name = 'tools/tool_list.html'
    context_object_name = 'tools'
    paginate_by = 10

    def get_queryset(self):
        queryset = Tool.objects.all()
        search = self.request.GET.get('search', '').strip()
        status = self.request.GET.get('status', '').strip().lower()

        if search:
            queryset = queryset.filter(tool_name__icontains=search)

        if status in [Tool.STATUS_ACTIVE, Tool.STATUS_INACTIVE]:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '').strip()
        context['status_filter'] = self.request.GET.get('status', '').strip().lower()
        return context


class ToolCreateView(LoginRequiredMixin, CreateView):
    model = Tool
    form_class = ToolForm
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:list')

    def form_valid(self, form):
        tool = form.save(commit=False)
        tool.created_by = self.request.user
        tool.updated_by = self.request.user
        tool.save()
        messages.success(self.request, 'Tool created successfully.')
        return redirect(self.success_url)


class ToolUpdateView(LoginRequiredMixin, UpdateView):
    model = Tool
    form_class = ToolForm
    template_name = 'tools/tool_form.html'
    success_url = reverse_lazy('tools:list')

    def form_valid(self, form):
        tool = form.save(commit=False)
        tool.updated_by = self.request.user
        tool.save()
        messages.success(self.request, 'Tool updated successfully.')
        return redirect(self.success_url)


class ToolDetailView(LoginRequiredMixin, DetailView):
    model = Tool
    template_name = 'tools/tool_detail.html'
    context_object_name = 'tool'


class ToolDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        tool = get_object_or_404(Tool, pk=pk)
        tool.is_deleted = True
        tool.updated_by = request.user
        tool.save(update_fields=['is_deleted', 'updated_by', 'updated_at'])
        messages.success(request, 'Tool deleted successfully.')
        return redirect('tools:list')

    def get(self, request, pk, *args, **kwargs):
        tool = get_object_or_404(Tool, pk=pk)
        return render(request, 'tools/delete_confirmation_modal.html', {'tool': tool})
