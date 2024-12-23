from django.db import models
import uuid

class Detection(models.Model):
    patient_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    adoption_date = models.DateField()  # Changed to DateField
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    upload_file = models.ImageField(upload_to='findings/', blank=True, null=True)
    covid_status = models.BooleanField(blank=True)
    pneumonia_status = models.BooleanField(blank=True)
    cancer_status = models.BooleanField(blank=True)

    def __str__(self):
        return f"{self.name}"
