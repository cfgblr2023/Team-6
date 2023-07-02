from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import *
import nexmo

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
    Courses=Course.objects.filter(CourseMentor=username)
    numberOfCourses=len(Courses)
    Courses=Courses.distinct()
    numberOfMentees=0
    for i in Courses:
        numberOfMentees+=len(CourseRelation.objects.filter(CourseID=i.CourseID))
    data={
        "numberOfCourses":numberOfCourses,
        "numberOfMentees":numberOfMentees
    }
    return render(request,"Mentor/mentorbase.html",data)

def mentee(request):
    username=""
    with open("temp.txt") as f:
        username=f.read()
    data={
        "username":username,
    }
    return render(request,"mentee/mentee.html",data)

def adminUser(request):
    return render(request,"admin/adminbase.html")

def adminMentor(request):
    return render(request,"admin/admin_mentor.html")
def adminMentee(request):
    return render(request,"admin/admin_mentee.html")
def adminCourse(request):
    return render(request,"admin/admin_course.html")


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
        f.close()

def totalStudents(request):
    username=""
    with open('temp.txt','r') as f:
        username=f
    # print(username)
    # Courses=Course.objects.filter(CourseMentor=username)
    # Courses=Courses.distinct()
    menteesList=[["jack","1234567890","jack@jack.com"],
                 ["priya","9123456780","priya@priya.com"],
                 ["suresh","9143256780","suresh@suresh.com"]]
    # print(Courses)
    # for i in Courses:
    #     menteesList.append(CourseRelation.objects.filter(CourseID=i.CourseID))
    data={
        "menteesList":menteesList
    }
    return render(request,'Mentor/totalStudents.html',data)
    


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        writeLogin(username)
        print(username)
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

    def sndSmsView():
        api_key = ""
        with open("api-key.txt", "a") as f:
            api_key += f.read()

        api_secret = ""
        with open("api-secret.txt", "a") as f:
            api_secret += f.read()

        client = nexmo.Client(key=api_key, secret=api_secret)
        phone_numbers = ['+919007088779']
        def send_sms_notification(phone_number):
            from_number = '+918904194092'  # Replace with your Nexmo phone number

        for phone_number in phone_numbers:
            send_sms_notification(phone_number)

        def send_sms_notification(phone_number):
            from_number = '+918904194092'  # Replace with your Nexmo phone number

            response = client.send_message({
                'from': from_number,
                'to': phone_number,
                'text': 'Hi from Py'
            })

            if response['messages'][0]['status'] == '0':
                print(f"SMS sent to {phone_number}. Message ID: {response['messages'][0]['message-id']}")
            else:
                print(f"Failed to send SMS to {phone_number}. Error: {response['messages'][0]['error-text']}")