from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from users import forms
from .forms import UploadFile
from django.contrib.auth.decorators import login_required

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
    path = 'uploads/{}.pdf'.format(request.user.id)
    
    if os.path.exists(path) == False:
        path = None
    else:
        path = '{}.pdf'.format(request.user.id)
    
    form = UploadFile()
    context = {
        'form':form,
        'path':path,
    }
    id = request.user.id
    if request.method == 'POST':
        handleUploadedFile(request.FILES['file'],id)
        return redirect('profile')


    return render(request,'users/profile.html',context)