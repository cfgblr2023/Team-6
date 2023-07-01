from views import *
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', view=home),
    path('login/',view=login),
    path('loginMentee/',view=loginMentee),
    path('loginMentor/',view=loginMentor),
    path('loginAdmin/',view=loginAdmin),
    path('registerMentee/',view=registerMentee),
    path('registerMentor/',view=registerMentor),
    path('mentor/',view=mentor),
    path('mentee/',view=mentee),
    path('admin/',view=adminUser),
    path('donate/',view=donate),
    path('jobPosting/',view=jobPosting)
]