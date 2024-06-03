from django.urls import path, include
from . import views

app_name = "HomeApp"

urlpatterns = [
    path('', views.ViewHome, name="HomeView"),
    ]
