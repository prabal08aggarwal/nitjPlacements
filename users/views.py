from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from users import forms
from .forms import UploadFile
from django.contrib.auth.decorators import login_required

from .forms import ResumeForm
from .models import Resume

import os.path
# Create your views here.

def register(request):
    if request.method == 'POST':
        form1 = UserCreationForm(request.POST)
        form2 = forms.StudentForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            
            firstName = form2.cleaned_data.get('firstName')
            student = form2.save(commit = False)
            user = form1.save(commit = False)

            student.user = user
            user.save() # Save into database
            student.save()
            
            messages.success(request,f'Account created for {firstName}!')
            return redirect('homePage')
    else:
        form1 = UserCreationForm()
        form2 = forms.StudentForm()

    context = {}
    context['form1'] = form1
    context['form2'] = form2
    return render(request,'users/register.html',context)


def handleUploadedFile(f,id):
    with open('uploads/{}.pdf'.format(id), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

#Auth views
@login_required
def profile(request):
    if request.method == 'POST':
        obj = Resume.objects.all().filter(user = request.user)
        if obj.exists():
            obj.delete()
        
        resume = ResumeForm()
        form1 = ResumeForm(request.POST)
        print(form1)
        resumeObj = form1.save(commit = False)
        resumeObj.user = request.user
        resumeObj.save()

    

    
    data = Resume.objects.all().filter(user = request.user)
    if data.exists():
        data = data[0]
        resume = ResumeForm(instance = data)
    else:
        data = None
        resume = ResumeForm()
    
    print(data)
    print("*******************************************")

    print("*******************************************")
    print("*******************************************")
    print("*******************************************")
    print("*******************************************")

    context = {
        'resumeForm':resume,
    }
    return render(request,'users/profile.html',context)