from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import EndUser
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            user = EndUser.objects.get(Username=username, Password=password)
            # Authentication successful
            request.session['user_id'] = user.id
            # You can add any additional session data here if needed
            return HttpResponse("Success")
        except EndUser.DoesNotExist:
            # Authentication failed
            return HttpResponse("Failure")

            # messages.error(request, 'Invalid username or password.')

    return render(request, 'home.html')

# Create your views here.

def home(request):
    return render(request, "home.html")

def loginUser(request):
    return render(request, "loginUser.html")

def loginMentee(request):
    return render(request,"mentee/mentee_login.html")

def loginMentor(request):
    return render(request,"Mentor/mentor_login.html")

def loginAdmin(request):
    return render(request,"admin_login.html")

def registerMentee(request):
    return render(request,"mentee/mentee_registration.html")

def registerMentor(request):
    return render(request,"Mentor/mentor_registration.html")

def mentor(request):
    return render(request,"mentor.html")

def mentee(request):
    return render(request,"mentee/mentee.html")

def adminUser(request):
    return render(request,"admin/adminbase.html")

def donate(request):
    return render(request,"")

def jobPosting(request):
    return render(request,"")






