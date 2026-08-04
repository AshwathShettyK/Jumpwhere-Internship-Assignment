from django.urls import path

from . import views

app_name = 'resume_generator'

urlpatterns = [
    path('', views.ResumeGeneratorView.as_view(), name='generate'),
    path('download/<int:pk>/', views.ResumeWordDownloadView.as_view(), name='download'),
    path('download/<int:pk>/pdf/', views.ResumePDFDownloadView.as_view(), name='download_pdf'),
]
