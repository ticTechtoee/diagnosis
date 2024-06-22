from django import forms
from .models import Detection

class DetectionForm(forms.ModelForm):
    class Meta:
        model = Detection
        fields = ['name', 'phone', 'email', 'adoption_date', 'age', 'gender', 'upload_file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Name'}),
            'phone': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}),
            'adoption_date': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Date of adoption'}),
            'age': forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'input-field'}, choices=[('male', 'Male'), ('female', 'Female')]),
            'upload_file': forms.ClearableFileInput(attrs={'class': 'upload-label'}),
            }
