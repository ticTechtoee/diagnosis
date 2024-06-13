from django.urls import path
from . import views

app_name = "AdminApp"

urlpatterns = [
    path('dashboard/', views.ViewAdminDashboard, name="DashboardView"),
    ]
