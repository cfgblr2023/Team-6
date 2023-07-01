from django.shortcuts import render
from django.http import HttpResponse
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






