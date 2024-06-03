from django.urls import path, include
from . import views

app_name = "AccountApp"

urlpatterns = [
    path('signup/', views.ViewSignup, name="SignupView"),
    path('login/', views.ViewLogin, name="LoginView"),

]
