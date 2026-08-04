from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import FormView, View
from io import BytesIO

from .forms import ResumeGeneratorForm
from .services import ResumeBuilderService
from .word_service import WordExportService
from .pdf_service import PDFExportService
from employees.models import Employee


class ResumeGeneratorView(LoginRequiredMixin, FormView):
    template_name = 'resume_generator/generator_form.html'
    form_class = ResumeGeneratorForm

    def get(self, request, *args, **kwargs):
        # UI wiring: If employee is requested in GET param, render the preview directly
        employee_id = request.GET.get('employee')
        if employee_id:
            try:
                context = ResumeBuilderService.get_resume_context(employee_id)
                return render(request, 'resume_generator/resume_preview.html', context)
            except Employee.DoesNotExist:
                messages.error(request, 'Employee record not found.')
                return redirect('resume_generator:generate')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        employee = form.cleaned_data['employee']
        context = ResumeBuilderService.get_resume_context(employee.pk)
        return render(self.request, 'resume_generator/resume_preview.html', context)


class ResumeWordDownloadView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        try:
            context = ResumeBuilderService.get_resume_context(pk)
        except Employee.DoesNotExist:
            return HttpResponse('Employee not found.', status=404)

        document = WordExportService.generate_docx(context)
        
        buffer = BytesIO()
        document.save(buffer)
        buffer.seek(0)

        filename = f'Resume_{context["employee"].first_name}_{context["employee"].last_name}.docx'.replace(' ', '_')
        response = HttpResponse(
            buffer.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response


class ResumePDFDownloadView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        try:
            context = ResumeBuilderService.get_resume_context(pk)
        except Employee.DoesNotExist:
            return HttpResponse('Employee not found.', status=404)

        buffer = PDFExportService.generate_pdf(context)

        filename = f'Resume_{context["employee"].first_name}_{context["employee"].last_name}.pdf'.replace(' ', '_')
        response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response
