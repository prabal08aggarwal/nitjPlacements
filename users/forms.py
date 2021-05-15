from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from users import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        data = email.split('@')
        
        if "nitj.ac.in" not in data:
            raise forms.ValidationError("Use NITJ Account")

        return email

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['firstName','lastName','email','rollNumber','program','department','year','ph_no']
    def clean_email(self):
        email = self.cleaned_data.get('email')

        data = email.split('@')
        
        if "nitj.ac.in" not in data:
            raise forms.ValidationError("Use NITJ Account")

        return email

class UploadFile(forms.Form):
    file = forms.FileField()


class ResumeForm(forms.ModelForm):
    class Meta:
        model = models.Resume
        fields = ['workExperience','education','projects','skills','achievements']

