from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "FormApp"

urlpatterns = [
    path('detect_disease/', views.ViewDetectDisease, name="DiseaseView"),
    path('detection_result/<str:pk>/', views.DetectionResultView, name='DetectionResultView'),
    ]
