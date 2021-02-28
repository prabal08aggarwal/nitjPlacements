from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from users import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['firstName','lastName','email','ph_no']
