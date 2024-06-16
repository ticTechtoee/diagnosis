from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib import messages
from django.conf import settings
from .forms import CustomUserCreationForm, CustomAuthenticationForm, PasswordResetRequestForm

CustomUser = get_user_model()

def ViewSignup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AccountApp:LoginView')
    else:
        form = CustomUserCreationForm()
    return render(request, "AccountApp/SignupView.html", {'form': form})

def ViewLogin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect("AdminApp:DashboardView")
                else:
                    return redirect('HomeApp:HomeView')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, "AccountApp/LoginView.html", {'form': form})

def ViewLogout(request):
    logout(request)
    return redirect("AccountApp:LoginView")

def ViewForgetPassword(request):
    if request.method == "POST":
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = CustomUser.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            password_reset_url = request.build_absolute_uri(f'/reset/{uid}/{token}/')

            context = {
                'email': user.email,
                'password_reset_url': password_reset_url,
            }
            subject = 'Password Reset Requested'
            email_template_name = 'AccountApp/password_reset_email.html'
            email_body = render_to_string(email_template_name, context)

            send_mail(subject, email_body, settings.DEFAULT_FROM_EMAIL, [user.email])
            return redirect('AccountApp:PasswordResetDoneView')
    else:
        form = PasswordResetRequestForm()
    return render(request, 'AccountApp/ForgetPasswordView.html', {'form': form})

def PasswordResetConfirmView(request, uidb64=None, token=None):
    if uidb64 is not None and token is not None:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(CustomUser, pk=uid)

        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = SetPasswordForm(user, request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('AccountApp:PasswordResetCompleteView')
            else:
                form = SetPasswordForm(user)
            return render(request, 'AccountApp/password_reset_confirm.html', {'form': form})
        else:
            return redirect('AccountApp:PasswordResetInvalidView')
    else:
        return redirect('AccountApp:PasswordResetInvalidView')

def PasswordResetDoneView(request):
    return render(request, "AccountApp/password_reset_done.html")

def PasswordResetCompleteView(request):
    return render(request, "AccountApp/password_reset_complete.html")

def PasswordResetInvalidView(request):
    return render(request, "AccountApp/password_reset_invalid.html")
