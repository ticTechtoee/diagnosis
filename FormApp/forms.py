from django import forms

class DetectionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Name'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Phone'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Email'}))
    adoption_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input-field', 'placeholder': 'Date of adoption'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Age'}))
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')],
        widget=forms.RadioSelect(attrs={'class': 'input-field'})
    )
    upload_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'upload-label'}))