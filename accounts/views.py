from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import *
from user_profile.models import UserProfile

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def about_us(request):
    return render(request, 'accounts/about_us.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + ' ' + last_name
            UserProfile.objects.create(name=name, user=user)
            login(request, user)
            return redirect('accounts:home')
    else:
        form = UserCreateForm()
    return render(request, 'accounts/register.html', {'form': form})