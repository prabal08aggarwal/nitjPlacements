from django import forms
from .models import interviewExp

class newExp(forms.ModelForm):
    class Meta:
        model = interviewExp
        fields = ['company','content']


class filterForm(forms.ModelForm):
    company = forms.CharField(max_length = 100,required = False)
    author = forms.CharField(max_length = 100,required = False)
    class Meta:
        model = interviewExp
        fields = ['company','author']