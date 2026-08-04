from django.urls import path

from . import views

app_name = 'tools'

urlpatterns = [
    path('', views.ToolListView.as_view(), name='list'),
    path('create/', views.ToolCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.ToolUpdateView.as_view(), name='edit'),
    path('<int:pk>/', views.ToolDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.ToolDeleteView.as_view(), name='delete'),
]
