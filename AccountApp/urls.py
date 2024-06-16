from django.urls import path
from . import views

app_name = 'AccountApp'

urlpatterns = [
    path('signup/', views.ViewSignup, name='SignupView'),
    path('login/', views.ViewLogin, name='LoginView'),
    path('logout/', views.ViewLogout, name='LogoutView'),
    path('forget-password/', views.ViewForgetPassword, name='ForgetPasswordView'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView, name='PasswordResetConfirmView'),
    path('password-reset-done/', views.PasswordResetDoneView, name='PasswordResetDoneView'),
    path('password-reset-complete/', views.PasswordResetCompleteView, name='PasswordResetCompleteView'),
    path('password-reset-invalid/', views.PasswordResetInvalidView, name='PasswordResetInvalidView'),
]
