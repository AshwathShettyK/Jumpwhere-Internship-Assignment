from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView, View
from django.shortcuts import redirect, render, get_object_or_404

from .forms import CodingForm
from .models import Coding


class CodingListView(LoginRequiredMixin, ListView):
    model = Coding
    template_name = 'coding/coding_list.html'
    context_object_name = 'codings'
    paginate_by = 10

    def get_queryset(self):
        queryset = Coding.objects.all()
        search = self.request.GET.get('search', '').strip()
        status = self.request.GET.get('status', '').strip().lower()

        if search:
            queryset = queryset.filter(coding_name__icontains=search)

        if status in [Coding.STATUS_ACTIVE, Coding.STATUS_INACTIVE]:
            queryset = queryset.filter(status=status)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '').strip()
        context['status_filter'] = self.request.GET.get('status', '').strip().lower()
        return context


class CodingCreateView(LoginRequiredMixin, CreateView):
    model = Coding
    form_class = CodingForm
    template_name = 'coding/coding_form.html'
    success_url = reverse_lazy('coding:list')

    def form_valid(self, form):
        coding = form.save(commit=False)
        coding.created_by = self.request.user
        coding.updated_by = self.request.user
        coding.save()
        messages.success(self.request, 'Coding skill created successfully.')
        return redirect(self.success_url)


class CodingUpdateView(LoginRequiredMixin, UpdateView):
    model = Coding
    form_class = CodingForm
    template_name = 'coding/coding_form.html'
    success_url = reverse_lazy('coding:list')

    def form_valid(self, form):
        coding = form.save(commit=False)
        coding.updated_by = self.request.user
        coding.save()
        messages.success(self.request, 'Coding skill updated successfully.')
        return redirect(self.success_url)


class CodingDetailView(LoginRequiredMixin, DetailView):
    model = Coding
    template_name = 'coding/coding_detail.html'
    context_object_name = 'coding'


class CodingDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        coding = get_object_or_404(Coding, pk=pk)
        coding.is_deleted = True
        coding.updated_by = request.user
        coding.save(update_fields=['is_deleted', 'updated_by', 'updated_at'])
        messages.success(request, 'Coding skill deleted successfully.')
        return redirect('coding:list')

    def get(self, request, pk, *args, **kwargs):
        coding = get_object_or_404(Coding, pk=pk)
        return render(request, 'coding/delete_confirmation_modal.html', {'coding': coding})
