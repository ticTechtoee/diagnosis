from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "FormApp"

urlpatterns = [
    path('detect_disease/', views.ViewDetectDisease, name="DiseaseView"),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
