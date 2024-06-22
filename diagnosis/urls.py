from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HomeApp.urls")),
    path('account/', include("AccountApp.urls")),
    path('form/', include("FormApp.urls")),
    path('services/', include("ServiceApp.urls")),
    path('manager/', include("AdminApp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
