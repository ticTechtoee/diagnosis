from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include("AccountApp.urls")),
    path('form/', include("FormApp.urls")),
    path('', include("HomeApp.urls")),
]
