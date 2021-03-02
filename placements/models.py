from django.db import models
from django.contrib.auth.models import User
from users import models as userModel
# Create your models here.


class company(models.Model):
    Name = models.CharField(max_length=256)
    JobDescription = models.TextField()
    title = models.CharField(max_length=200, null=False)
    

    def __str__(self):
        return self.Name 

class jobAppication(models.Model):
    student = models.ForeignKey(userModel.Student,on_delete=models.CASCADE)
    AppliedTo = models.ForeignKey(company,on_delete=models.CASCADE)