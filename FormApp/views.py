import os
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from .forms import DetectionForm
from django.contrib.staticfiles import finders
from tensorflow.keras.models import load_model
import cv2
import numpy as np


from .models import Detection


IMAGE_SIZE = (224, 224)
LABELS_COVID = ['COVID', 'Non-COVID', 'Pneumonia']
LABELS_LUNG = ['Lung_cancer', 'Normal']

def load_trained_model(model_path):
    return load_model(model_path)

def preprocess_image(image_path):
    img_array = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img_array = cv2.resize(img_array, IMAGE_SIZE)
    img_array = img_array.reshape(-1, IMAGE_SIZE[0], IMAGE_SIZE[1], 1)
    img_array = img_array / 255.0
    return img_array

def predict_image(model, image_path, labels):
    img_array = preprocess_image(image_path)
    prediction = model.predict(img_array)
    return labels[np.argmax(prediction)]

def ViewDetectDisease(request):
    if request.method == 'POST':
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            detection_instance = form.save(commit=False)

            # Save the uploaded file to get the path
            uploaded_file = request.FILES['upload_file']
            save_dir = 'media/findings'
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)

            file_path = os.path.join(save_dir, uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            # Determine which model to use based on file extension
            if uploaded_file.name.lower().endswith('.jpg'):
                model_path = finders.find('assets/models/covid_model.h5')
                labels = ['COVID', 'Non-COVID', 'Pneumonia']
            else:
                model_path = finders.find('assets/models/lung_model.h5')
                labels = ['Lung_cancer', 'Normal']

            if model_path is None:
                raise ValueError("Model file not found. Check if the model files are correctly placed in the static directory.")

            # Load the model
            model = load_trained_model(model_path)

            # Perform prediction
            result = predict_image(model, file_path, labels)

            # Update statuses based on prediction result
            if result == 'COVID':
                detection_instance.covid_status = True
                detection_instance.pneumonia_status = False
                detection_instance.cancer_status = False
            elif result == 'Pneumonia':
                detection_instance.covid_status = False
                detection_instance.pneumonia_status = True
                detection_instance.cancer_status = False
            elif result == 'Lung_cancer':
                detection_instance.covid_status = False
                detection_instance.pneumonia_status = False
                detection_instance.cancer_status = True
            else:
                detection_instance.covid_status = False
                detection_instance.pneumonia_status = False
                detection_instance.cancer_status = False

            # Save the detection instance with updated statuses
            detection_instance.save()

            # Redirect to DetectionResult view with detection instance ID
            return redirect('FormApp:DetectionResultView', pk=detection_instance.patient_id)
        else:
            print(form.errors)
    else:
        form = DetectionForm()

    return render(request, "FormApp/DetectDisease.html", {'form': form, 'title': 'Detection'})

def DetectionResultView(request, pk):
    detection_instance = get_object_or_404(Detection, patient_id=pk)

    # Prepare context to pass to template
    context = {
        'detection_instance': detection_instance,
    }

    return render(request, 'FormApp/DetectionResult.html', context)