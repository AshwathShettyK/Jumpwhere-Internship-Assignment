from django.urls import path
from . import views

app_name = "dictionary"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("search/", views.search_view, name="search"),
    path("word/<str:word>/", views.word_detail_view, name="detail"),
]
