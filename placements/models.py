from django.db import models
from django.contrib.auth.models import User
from users import models as userModel
from multiselectfield import MultiSelectField
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

empType = (
    ("intern","Internship"),
    ("fte","Full Time")
)

class company(models.Model):
    Name = models.CharField(max_length=256)
    JobDescription = models.TextField()
    title = models.CharField(max_length=200, null=False)
    departmentsEligible =  MultiSelectField(choices=departmentChoice,default = "cse")
    programEligible = MultiSelectField(choices=programChoice,default = "BTech")
    employmentType = models.CharField(choices=empType,max_length=200,null = True,blank=True)
    package = models.IntegerField(null = True,blank = True)

    def __str__(self):
        return self.Name 

class jobAppication(models.Model):
    student = models.ForeignKey(userModel.Student,on_delete=models.CASCADE)
    AppliedTo = models.ForeignKey(company,on_delete=models.CASCADE)