from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from users import models as user_model
# Create your models here.

class interviewExp(models.Model):
    company = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(user_model.Student,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.company