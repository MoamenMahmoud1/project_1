from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import Login
from .middleware import RestrictIPMiddleware
from asgiref.sync import sync_to_async
from django.db import connection

class Inputs:
    """Utility class to handle input validation."""
    @staticmethod
    def username(request):
        return request.POST.get('username', '')

    @staticmethod
    def password(request):
        return request.POST.get('passw', '')

def index(request):
    context = {'name': 'Joe'}
    return render(request, 'index.html', context)

@csrf_exempt
async def login(request):
    """Login view."""
    if request.method == 'POST':
        username = Inputs.username(request)
        password = Inputs.password(request)

        if not username or not password:
            return render(request, 'about.html', {'error': 'Please enter both username and password.'})

        invalid_characters = set('/<>')
        if any(char in invalid_characters for char in username + password):
            return render(request, 'about.html', {'error': 'Your username or password contains invalid characters.'})

        if len(username) < 5:
            return render(request, 'about.html', {'error': 'Your username is too short. It must be at least 5 characters long.'})

        if len(password) < 5:
            return render(request, 'about.html', {'error': 'Your password is too short. It must be at least 5 characters long.'})

        if password == username:
            return render(request, 'about.html', {'error': 'Your password cannot be the same as your username.'})

        exists = await sync_to_async(lambda: Login.objects.filter(username=username, password=password).exists(), thread_sensitive=True)()
        if exists:
            return render(request, 'about.html', {'error': 'This username is already in use. Please choose a different username.'})

        await sync_to_async(lambda: Login.objects.create(username=username, password=password), thread_sensitive=True)()

    return render(request, 'about.html')

def signup(request):
    return render(request, 'signup.html')

async def main(request):
    username = Inputs.username(request)
    password = Inputs.password(request)
    
    exists = await sync_to_async(Login.objects.filter(username=username, password=password).exists)()
    if exists:
        return render(request, 'main.html')
    else:
        return HttpResponseNotFound("")

def about_view(request, year):
    year_str = str(year)
    if len(year_str) == 4 and year_str.isdigit():
        return HttpResponse(f"أنت تتصفح صفحة عن السنة: {year_str}")
    else:
        return HttpResponseNotFound("الرابط غير صحيح، يجب أن يكون السنة مكونة من 4 أرقام.")

def contact(request, id):
    pass

def add_ip_view(request):
    if request.method == "POST":
        new_ip = request.POST.get('ip_address')
        middleware = RestrictIPMiddleware(lambda request: None)
        message = middleware.add_allowed_ip(new_ip)
        return HttpResponse(message)

    return render(request, 'add_ip.html')

def special_view(request):
    return HttpResponse("This is a special page.")

