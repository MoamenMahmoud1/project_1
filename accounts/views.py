from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import logout
import re



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the email is a valid Gmail address
        if not email.endswith('@gmail.com'):
            return HttpResponse("Please enter a valid Gmail address.")
        
        # Authenticate the user using the email (username) and password
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            return HttpResponse("Invalid credentials")
    
    return render(request, 'accounts/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the email is a valid Gmail address
        if not email.endswith('@gmail.com'):
            return HttpResponse("Please enter a valid Gmail address.")

        # Create the user in the database if the email is valid
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Redirect to login page after successful sign-up
        except Exception as e:
            return HttpResponse(f"Error creating user: {e}")
    
    return render(request, 'accounts/signup.html')



def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

