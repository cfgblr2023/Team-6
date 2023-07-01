from django.contrib import admin
from .models import EndUser, Course, CourseRelation

# Register your models here.
admin.site.register(EndUser)
admin.site.register(Course)
admin.site.register(CourseRelation)
