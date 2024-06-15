from django.urls import path
from . import views

app_name = "AdminApp"

urlpatterns = [
    path('dashboard/', views.ViewAdminDashboard, name="DashboardView"),
    path('manage/', views.ViewManageAccounts, name="ManageAccountsView"),
    path('delete/<int:pk>/', views.ViewDeleteUser, name="DeleteUserView"),
    path('patients/', views.ViewPatientList, name="PatientListView"),
    path('delete_patient/<int:pk>', views.ViewDeletePatient, name="DeletePatienView")
    ]
