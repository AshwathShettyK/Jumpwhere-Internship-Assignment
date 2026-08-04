from django.urls import path

from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='edit'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='delete'),
    path('assignments/', views.EmployeeProjectListView.as_view(), name='assignments_list'),
    path('assignments/create/', views.EmployeeProjectCreateView.as_view(), name='assignments_create'),
    path('assignments/<int:pk>/edit/', views.EmployeeProjectUpdateView.as_view(), name='assignments_edit'),
    path('assignments/<int:pk>/', views.EmployeeProjectDetailView.as_view(), name='assignments_detail'),
    path('assignments/<int:pk>/delete/', views.EmployeeProjectDeleteView.as_view(), name='assignments_delete'),
]
