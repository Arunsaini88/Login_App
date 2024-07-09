from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignupForm, LoginForm, ProfilePictureForm
from .models import User, Patient, Doctor
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            pass1 = form.cleaned_data.get('password1')
            print(pass1)
            pass2 = form.cleaned_data.get('password2')
            print(pass2)
            if pass1 != pass2:
                form.add_error('passwoed2','Password doesn`t match')
            else:
                user.set_password(form.cleaned_data.get('password1'))
                user.save()
                user_type = form.cleaned_data.get('user_type')
                if user_type == 'Patient':
                    Patient.objects.create(user=user)
                    user.is_patient = True
                else:
                    Doctor.objects.create(user=user)
                    user.is_doctor = True
                user.save()
                return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                if user.is_patient:
                    return redirect('patient_dashboard')
                elif user.is_doctor:
                    return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def patient_dashboard(request):
    user = request.user
    if not user.is_authenticated or not user.is_patient:
        return redirect('login')
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('patient_dashboard')
    else:
        form = ProfilePictureForm(instance=user)
    return render(request, 'patient_dashboard.html', {'user': user, 'form': form})

def dashboard(request):
    user = request.user
    if not user.is_authenticated or not user.is_doctor:
        return redirect('login')
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfilePictureForm(instance=user)
    return render(request, 'dashboard.html', {'user': user, 'form': form})
