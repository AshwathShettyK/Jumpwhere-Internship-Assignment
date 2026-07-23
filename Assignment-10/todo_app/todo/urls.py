from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.task_list, name="home"),
    path("task/add/", views.task_add, name="add"),
    path("task/<int:pk>/", views.task_detail, name="detail"),
    path("task/<int:pk>/edit/", views.task_edit, name="edit"),
    path("task/<int:pk>/delete/", views.task_delete, name="delete"),
    path("task/<int:pk>/toggle/", views.task_toggle, name="toggle"),
]
