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

def loginMentee(request):
    return render(request,"mentee_login.html")

def loginMentor(request):
    return render(request,"mentor_login.html")

def loginAdmin(request):
    return render(request,"admin_login.html")

def registerMentee(request):
    return render(request,"mentee_register.html")

def registerMentor(request):
    return render(request,"mentor_register.html")

def mentor(request):
    return render(request,"mentor.html")

def mentee(request):
    return render(request,"mentee.html")

def adminUser(request):
    return render(request,"admin.html")

def donate(request):
    return render(request,"")

def jobPosting(request):
    return render(request,"")

def adminbase(request):
    return render(request, "adminbase.html")






