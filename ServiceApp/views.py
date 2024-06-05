from django.shortcuts import render

def ViewIndex(request):
    return render(request, "ServiceApp/IndexView.html")
