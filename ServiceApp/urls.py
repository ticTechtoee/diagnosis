from django.urls import path
from . import views

app_name = "ServiceApp"

urlpatterns = [
    path('', views.ViewIndex, name="IndexView"),
    ]
