from django.db import models

class Detection(models.Model):
    DETECTION_TYPE_CHOICES = [
        ('covid', 'Covid-19'),
        ('lungcancer', 'Lung Cancer'),
        ('pneumonia', 'Pneumonia'),
    ]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    adoption_date = models.CharField(max_length=100)  # Changed to CharField
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    upload_file = models.FileField(upload_to='uploads/')
    detection_type = models.CharField(max_length=10, choices=DETECTION_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.get_detection_type_display()}"
