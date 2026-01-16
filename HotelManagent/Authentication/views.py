from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib import messages
from Authentication.forms import CustomUserCreationForm

# Home 
def home(request):
    return render(request, 'Authentication/home.html')


# Signup Service
def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'Authentication/signup.html', context)


# Login function
def login_user(request):
    if request.method=='POST':
        email= request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))

        else:
            messages.error(request, "invalid password or email address")
    return render(request, 'Authentication/login.html')


# logout function
def logout_user(request):
    logout(request)
    return redirect(reverse('home'))