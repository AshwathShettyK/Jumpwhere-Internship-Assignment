from django.urls import path
from . import views

app_name = "shortener"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("result/<str:short_code>/", views.result_view, name="result"),
    path("<str:short_code>/", views.redirect_view, name="redirect"),
]
