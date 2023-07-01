from django.contrib import admin
from .models import User, Course, CourseRelation

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('Username', 'Name', 'Password', 'PhoneNumber', 'Permission', 'Email')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('CourseID', 'CourseName', 'CourseCategory', 'CourseDescription', 'CourseMentor', 'CourseMentee')

class CourseRelationAdmin(admin.ModelAdmin):
    list_display = ('Mentor', 'Mentee', 'CourseStatus')