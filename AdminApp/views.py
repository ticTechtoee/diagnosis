from django.shortcuts import render

def ViewAdminDashboard(request):
    return render(request, "AdminApp/AdminDashboard.html")