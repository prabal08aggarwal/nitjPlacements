from django.db import models
from django.contrib.auth.models import User
from users import models as userModel
from multiselectfield import MultiSelectField
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

empType = (
    ("Internship","Internship"),
    ("Full Time","Full Time")
)

class company(models.Model):
    Name = models.CharField(max_length=256)
    JobDescription = RichTextField()
    title = models.CharField(max_length=200, null=False)
    departmentsEligible =  MultiSelectField(choices=departmentChoice,default = "Computer Science")
    programEligible = MultiSelectField(choices=programChoice,default = "BTech")
    employmentType = models.CharField(choices=empType,max_length=200,null = True,blank=True)
    package = models.IntegerField(null = True,blank = True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.Name 

class jobAppication(models.Model):
    student = models.ForeignKey(userModel.Student,on_delete=models.CASCADE)
    AppliedTo = models.ForeignKey(company,on_delete=models.CASCADE)