from django.urls import path

from . import views

app_name = 'coding'

urlpatterns = [
    path('', views.CodingListView.as_view(), name='list'),
    path('create/', views.CodingCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.CodingUpdateView.as_view(), name='edit'),
    path('<int:pk>/', views.CodingDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.CodingDeleteView.as_view(), name='delete'),
]
