from django.db import models
from django.db import models
from users import models as user_model

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(user_model.Student, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

class Response(models.Model):
    user = models.ForeignKey(user_model.Student, null=False, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE, related_name='responses')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_responses(self):
        return Response.objects.filter(parent=self)
