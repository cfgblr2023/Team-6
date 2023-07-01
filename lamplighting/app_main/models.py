from django.db import models

# Create your models here.
class EndUser(models.Model):
    Username= models.CharField(max_length=25)
    Name= models.CharField(max_length=25)
    Password= models.CharField(max_length=100)
    PhoneNumber= models.IntegerField(max_length=10)
    Permission= models.CharField(max_length=25)
    Email= models.CharField(max_length=25)

class Course(models.Model):
    CourseID = models.CharField(max_length=25, primary_key=True)
    CourseName = models.CharField(max_length=25)
    CourseCategory = models.CharField(max_length=25)
    CourseDescription = models.CharField(max_length=100)
    CourseFeedback = models.CharField(max_length=25,default="NA")
    CourseMentor = models.CharField(max_length=25)
    CourseMentee = models.CharField(max_length=25)

class CourseRelation(models.Model):
    Mentor = models.CharField(max_length=25)
    Mentee = models.CharField(max_length=25)