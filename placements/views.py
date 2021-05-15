from django.shortcuts import render, redirect
from .models import company, jobAppication
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.
today = date.today()

@login_required
def index(request):
    companies = company.objects.all()
    applications = jobAppication.objects.all()

    applications = applications.filter(student = request.user.student)
    
    #get Company List
    applications = applications.values_list('AppliedTo',flat = True)
    
    eligible = []

    # Student data
    year = request.user.student.year
    program = request.user.student.program
    department = request.user.student.department

    # print(program)
    # print(department)
    check = []

    for comp in companies:
        departmentEligible = str(comp.departmentsEligible).split(', ')
        programEligible = str(comp.programEligible).split(', ')
        employmentType = str(comp.employmentType)
        check.append(comp.id)
        if program in programEligible and department in departmentEligible:
            if employmentType == "Full Time":
                if program == "MTech":
                    if year+2 == today.year:
                        eligible.append(comp.id)
                    elif year+1 == today.year and today.month > 6:
                        eligible.append(comp.id)
                elif program == "BTech":
                    if year+4 == today.year:
                        eligible.append(comp.id)
                    elif year+3 == today.year and today.month > 6:
                        eligible.append(comp.id)
            elif employmentType == "Internship":
                if program == "MTech":
                    if year == today.year:
                        eligible.append(comp.id)
                    elif year+1 == today.year and today.month < 6:
                        eligible.append(comp.id)
                elif program == "BTech":
                    if year+2 == today.year and today.month > 6:
                        eligible.append(comp.id)
                    elif year+3 == today.year and today.month < 6:
                        eligible.append(comp.id)
            else:
                eligible.append(comp.id)
    
    print(eligible)
    print(check)

    context = {
        'companies':companies,
        'appliedTo':applications,
        'eligible':eligible,
    }
    
    return render(request,'placements/index.html',context)


@login_required
def apply(request,idx):
    qs = company.objects.all()
    qs = qs.filter(id = idx).first()

    eligible = []

    # Student data
    year = request.user.student.year
    program = request.user.student.program
    department = request.user.student.department

    # print(program)
    # print(department)
    check = []
    companies = company.objects.all()
    for comp in companies:
        departmentEligible = str(comp.departmentsEligible).split(', ')
        programEligible = str(comp.programEligible).split(', ')
        employmentType = str(comp.employmentType)
        check.append(comp.id)
        if program in programEligible and department in departmentEligible:
            if employmentType == "Full Time":
                if program == "MTech":
                    if year+2 == today.year:
                        eligible.append(comp.id)
                    elif year+1 == today.year and today.month > 6:
                        eligible.append(comp.id)
                elif program == "BTech":
                    if year+4 == today.year:
                        eligible.append(comp.id)
                    elif year+3 == today.year and today.month > 6:
                        eligible.append(comp.id)
            elif employmentType == "Internship":
                if program == "MTech":
                    if year == today.year:
                        eligible.append(comp.id)
                    elif year+1 == today.year and today.month < 6:
                        eligible.append(comp.id)
                elif program == "BTech":
                    if year+2 == today.year and today.month > 6:
                        eligible.append(comp.id)
                    elif year+3 == today.year and today.month < 6:
                        eligible.append(comp.id)
            else:
                eligible.append(comp.id)
 

    if qs is not None and idx in eligible:
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

