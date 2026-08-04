from django.urls import path

from . import views

app_name = 'designations'

urlpatterns = [
    path('', views.DesignationListView.as_view(), name='list'),
    path('create/', views.DesignationCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.DesignationUpdateView.as_view(), name='edit'),
    path('<int:pk>/', views.DesignationDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.DesignationDeleteView.as_view(), name='delete'),
]
