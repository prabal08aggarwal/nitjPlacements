from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

programChoice = (
    ("BTech","Btech"),
    ("Mtech","Mtech"),
)

departmentChoice = (
    ("BT","Bio Technology"),
    ("che","Chemical"),
    ("chem","Chemistry"),
    ("civil","Civil"),
    ("cse","Computer Science"),
    ("elec","Electrical"),
    ("ece","Electronics and Communication"),
    ("ipe","Industial and Production"),
    ("it","Information Technology"),
    ("ice","Instrumentation and Control"),
    ("maths","Mathematics"),
    ("phe","Physics"),
    ("tt","Texttile Technology"),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.EmailField()
    ph_no = models.CharField(max_length=10)
    rollNumber = models.IntegerField()
    program = models.CharField(max_length = 5,default = 'Btech',choices = programChoice)
    department = models.CharField(max_length = 30,default = 'cse',choices = departmentChoice)
    year = models.IntegerField(default = 2017)

    def __str__(self):
        return self.firstName + " " + self.lastName 


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    workExperience = RichTextField(blank = True,null = True)
    education = RichTextField(blank = True,null = True)
    projects = RichTextField(blank = True,null = True)
    skills = RichTextField(blank = True,null = True)
    achievements = RichTextField(blank = True,null = True)


# class Resume(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     workExp = models.TextField(null = True)
#     education = models.TextField(null = True)
#     projects = models.TextField(null = True)
#     skills = models.TextField(null = True)
#     achievements = models.TextField(null = True)



