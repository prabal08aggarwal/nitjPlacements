from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

programChoice = (
    ("BTech","BTech"),
    ("MTech","MTech"),
)

departmentChoice = (
    ("Bio Technology","Bio Technology"),
    ("Chemical","Chemical"),
    ("Chemistry","Chemistry"),
    ("Civil","Civil"),
    ("Computer Science","Computer Science"),
    ("Electrical","Electrical"),
    ("Electronics and Communication","Electronics and Communication"),
    ("Industial and Production","Industial and Production"),
    ("Information Technology","Information Technology"),
    ("Instrumentation and Control","Instrumentation and Control"),
    ("Mathematics","Mathematics"),
    ("Physics","Physics"),
    ("Texttile Technology","Texttile Technology"),
)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.EmailField()
    ph_no = models.CharField(max_length=10)
    rollNumber = models.IntegerField()
    program = models.CharField(max_length = 5,default = 'BTech',choices = programChoice)
    department = models.CharField(max_length = 40,default = "Computer Science",choices = departmentChoice)
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



