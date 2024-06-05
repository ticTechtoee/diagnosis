from django.shortcuts import render

def ViewHome(request):
    return render(request, "HomeApp/IndexView.html")

def ViewAboutUs(request):
    return render(request, "HomeApp/AboutusView.html")