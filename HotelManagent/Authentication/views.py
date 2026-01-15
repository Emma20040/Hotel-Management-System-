from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse
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