from django.db import models

# Create your models here.
class User(models.Model):
    Username= models.CharField(max_length=25)
    Name= models.CharField(max_length=25)
    Password= models.CharField(max_length=100)
    PhoneNumber= models.IntegerField(max_length=10)
    Permission= models.CharField(max_length=25)
    Email= models.CharField(max_length=25)