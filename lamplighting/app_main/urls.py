from views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', view=home),
    path('loginMentee/',view=loginMentee),
    path('loginMentor/',view=loginMentor),
    path('loginAdmin/',view=loginAdmin),
    path('registerMentee/',view=registerMentee),
    path('registerMentor/',view=registerMentor),
    path('registerAdmin/',view=registerAdmin),
    path('mentor/',view=mentor),
    path('mentee/',view=mentee),
    path('admin/',view=adminUser),
    path('donate/',view=donate),
    path('jobPosting/',view=jobPosting)
]