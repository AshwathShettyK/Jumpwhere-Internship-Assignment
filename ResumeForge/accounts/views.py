from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import HRLoginForm, HRRegistrationForm
from .services import AuthService

def login_view(request):
    """
    Renders login screen and handles HR authentication logic via AuthService.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = HRLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = AuthService.authenticate_user(request, username=username, password=password)
            if user is not None:
                AuthService.login_user(request, user, remember_me=remember_me)
                messages.success(request, 'Successfully logged in. Welcome to ResumeForge!')
                # Respect standard next parameter redirect if present
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('dashboard:home')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Please correct the errors in the form.')

    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    """
    Renders registration page and manages HR user creation using AuthService.
    """
    if request.user.is_authenticated:
        return redirect('dashboard:home')

    form = HRRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = AuthService.register_user(form)
            # Authenticate the user and log them in immediately
            AuthService.login_user(request, user, remember_me=False)
            messages.success(request, 'Registration successful! Welcome to the HR Management Portal.')
            return redirect('dashboard:home')
        else:
            messages.error(request, 'Registration failed. Please see validation details below.')

    return render(request, 'accounts/register.html', {'form': form})

@login_required(login_url='accounts:login')
def logout_view(request):
    """
    Terminates user session and redirects to the login screen.
    """
    AuthService.logout_user(request)
    messages.info(request, 'You have successfully logged out of ResumeForge.')
    return redirect('accounts:login')
