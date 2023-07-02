"""lamplighting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', view=home),
    path('loginUser/',view=loginUser),
    path('loginMentee/',view=loginMentee),
    path('loginMentor/',view=loginMentor),
    path('loginMentee/login_view',view=login_view),
    path('loginMentor/login_view',view=login_view),
    path('loginAdmin/',view=loginAdmin),
    path('registerMentee/',view=registerMentee),
    path('registerMentor/',view=registerMentor),
    path('mentor/',view=mentor),
    path('mentee/',view=mentee),
    path('adminUser/',view=adminUser),
    path('donate/',view=donate),
    path('jobPosting',view=jobPosting),
    path('logoutUser/',view=logoutUser),
    path('video/',view=video)
    # path('adminbase/',view=adminbase)

]
