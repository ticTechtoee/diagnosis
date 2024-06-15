from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from AccountApp.models import CustomUser
from django.http import Http404
def ViewAdminDashboard(request):
    return render(request, "AdminApp/AdminDashboard.html")

def ViewManageAccounts(request):
    CustomUser = get_user_model()
    # Exclude admin users. Assuming 'is_superuser' flag is used to determine admin users
    get_accounts = CustomUser.objects.filter(is_superuser=False)

    context = {"Users": get_accounts if get_accounts.exists() else None}
    return render(request, "AdminApp/ManageAccounts.html", context)

def ViewDeleteUser(request, pk):
    CustomUser = get_user_model()
    try:
        get_user = CustomUser.objects.get(id=pk)
        get_user.delete()
    except CustomUser.DoesNotExist:
        raise Http404("User does not exist")

    return redirect('AdminApp:ManageAccountsView')