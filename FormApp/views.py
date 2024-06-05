from django.shortcuts import render
from .forms import DetectionForm

def ViewCovid(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle form processing here
            pass
    else:
        form = DetectionForm()
    return render(request, "FormApp/CovidFormView.html", {'form': form})

def ViewLung(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle form processing here
            pass
    else:
        form = DetectionForm()
    return render(request, "FormApp/LungFormView.html", {'form': form})

def ViewPneumonia(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle form processing here
            pass
    else:
        form = DetectionForm()
    return render(request, "FormApp/PneumoniaFormView.html", {'form': form})