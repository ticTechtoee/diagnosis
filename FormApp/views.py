from django.shortcuts import render
from .forms import CovidDetectionForm, LungCancerDetectionForm, PneumoniaDetectionForm

def ViewCovid(request):
    if request.method == 'POST':
        form = CovidDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle form processing here
            pass
        else:
            print(form.errors)
    else:
        form = CovidDetectionForm()

    return render(request, "FormApp/LungFormView.html", {'form': form, 'title': 'Covid-19 Detection'})

def ViewLung(request):
    if request.method == 'POST':
        form = LungCancerDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle form processing here
            pass
        else:
            print(form.errors)
    else:
        form = LungCancerDetectionForm()

    return render(request, "FormApp/LungFormView.html", {'form': form, 'title': 'Lung Cancer Detection'})

def ViewPneumonia(request):
    if request.method == 'POST':
        form = PneumoniaDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Handle form processing here
            pass
        else:
            print(form.errors)
    else:
        form = PneumoniaDetectionForm()

    return render(request, "FormApp/LungFormView.html", {'form': form, 'title': 'Pneumonia Detection'})
