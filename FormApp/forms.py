from django import forms
from .models import Detection

class DetectionForm(forms.ModelForm):
    class Meta:
        model = Detection
        fields = ['name', 'phone', 'email', 'adoption_date', 'age', 'gender', 'upload_file', 'detection_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Name'}),
            'phone': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}),
            'adoption_date': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Date of adoption'}),
            'age': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'input-field'}, choices=[('male', 'Male'), ('female', 'Female')]),
            'upload_file': forms.ClearableFileInput(attrs={'class': 'upload-label'}),
            'detection_type': forms.HiddenInput(),
        }

# Specific forms for each detection type
class CovidDetectionForm(DetectionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detection_type'].initial = 'covid'

class LungCancerDetectionForm(DetectionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detection_type'].initial = 'lungcancer'

class PneumoniaDetectionForm(DetectionForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['detection_type'].initial = 'pneumonia'
