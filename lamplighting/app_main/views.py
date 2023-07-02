from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import *

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
    username=""
    with open("temp.txt") as f:
        username=f.read()
    numberOfCourses=len(Course.objects.filter(CourseMentor=username))
    numberOfMentees=len(Course.objects.filter(CourseMentor=username))
    data={
        "numberOfCourses":numberOfCourses,
        "numberOfMentees":numberOfMentees
    }
    return render(request,"Mentor/mentorbase.html",data)

def mentee(request):
    return render(request,"mentee/mentee.html")

def adminUser(request):
    return render(request,"admin/adminbase.html")

def donate(request):
    return render(request,"")

def jobPosting(request):
    return render(request,"")

def video(request):
    return render(request,"mentee/video.html")

def logoutUser(request):
    request.session.flush()
    return HttpResponse("Logged out")
    return redirect('home')

def writeLogin(username):
    with open('temp.txt','w') as f:
        f.write(username)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        writeLogin(username)
        user = authenticate(request, username=username, password=password)
        try:
            user = EndUser.objects.get(Username=username, Password=password)
            request.session['user_id']=user.id
            # You can add any additional session data here if needed
            if(user.Permission=='m'):
                return redirect('/mentor/')
            if(user.Permission=='a'):
                return redirect('/adminbase/')
            return redirect('/mentee/')
            
        except EndUser.DoesNotExist:
            # Authentication failed
            return redirect('/home/')


            # messages.error(request, 'Invalid username or password.')

