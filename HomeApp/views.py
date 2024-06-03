from django.shortcuts import render

# Create your views here.
def ViewHome(request):
    return render(request, "HomeApp/IndexView.html")