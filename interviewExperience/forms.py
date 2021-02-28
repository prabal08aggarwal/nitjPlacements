from django import forms
from .models import interviewExp

class newExp(forms.ModelForm):
    class Meta:
        model = interviewExp
        fields = ['company','content']