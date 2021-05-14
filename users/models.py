from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.EmailField()
    ph_no = models.CharField(max_length=10)

    def __str__(self):
        return self.firstName + " " + self.lastName 


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workExp = models.TextField(null = True)
    education = models.TextField(null = True)
    projects = models.TextField(null = True)
    skills = models.TextField(null = True)
    achievements = models.TextField(null = True)


