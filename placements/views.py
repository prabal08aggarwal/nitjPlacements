from django.shortcuts import render, redirect
from .models import company, jobAppication
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    companies = company.objects.all()
    applications = jobAppication.objects.all()

    applications = applications.filter(student = request.user.student)
    
    #get Company List
    applications = applications.values_list('AppliedTo',flat = True)
 

    context = {
        'companies':companies,
        'appliedTo':applications
    }
    
    return render(request,'placements/index.html',context)


@login_required
def apply(request,idx):
    qs = company.objects.all()
    qs = qs.filter(id = idx).first()

    if qs is not None:
        application = jobAppication(student = request.user.student, AppliedTo = qs)
        application.save()
    
    return redirect('jobPortal')

@login_required
def applied(request):
    companies = company.objects.all()
    applications = jobAppication.objects.all()

    applications = applications.filter(student = request.user.student)
    
    #get Company List
    applications = applications.values_list('AppliedTo',flat = True)
 

    context = {
        'companies':companies,
        'appliedTo':applications
    }
    
    return render(request,'placements/applied.html',context)

