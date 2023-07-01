from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
        else:
            # Show an error message
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password.'})
    return render(request, 'accounts/login.html')

# Create your views here.

def home(request):
    return render(request, "home.html")

