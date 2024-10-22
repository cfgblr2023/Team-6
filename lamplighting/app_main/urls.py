from views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', view=home),
    path('login/',view=login),
    path('loginMentee/',view=loginMentee),
    path('loginMentee/login_view',view=login_view),
    path('loginMentor/login_view',view=login_view),
    path('loginAdmin/',view=loginAdmin),
    path('registerMentee/',view=registerMentee),
    path('registerMentor/',view=registerMentor),
    path('mentor/',view=mentor),
    path('mentor/totalStudents',view=totalStudents),
    path('mentee/',view=mentee),
    path('adminUser/',view=adminUser),
    path('donate/',view=donate),
    path('jobPosting/',view=jobPosting),
    path('video/',view=video),
    path('logoutUser/',view=logoutUser),
    path('adminMentor/',view=adminMentor),
    path('adminMentee/',view=adminMentee),
    path('adminCourse/',view=adminCourse)
    # path('adminbase/',view=adminbase)
]