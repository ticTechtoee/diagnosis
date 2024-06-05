from django.urls import path
from . import views

app_name = "FormApp"

urlpatterns = [
    path('covid/', views.ViewCovid, name="CovidView"),
    path('lung/', views.ViewLung, name="LungView"),
    path('pneumonia/', views.ViewPneumonia, name="PneumoniaView"),
    ]
