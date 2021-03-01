from django.shortcuts import render,redirect
from .models import interviewExp

from django.contrib.auth.decorators import login_required

from .forms import newExp

from .forms import filterForm
# Create your views here.

@login_required
def index(request):
    form = filterForm()
    qs = interviewExp.objects.all()

    company = request.GET.get('company')
    authorName = request.GET.get('author')
    
    if company is not None and company != '':
        qs = qs.filter(company__icontains = company)

    if authorName is not None and authorName != '':
        qs = qs.filter(author__firstName__icontains = authorName)

   
    context = {
        'form':form,
        'interviewExp':qs
    }

    return render(request,'interviewExperience/index.html',context)

@login_required
def newExpview(request):
    form = newExp()

    if request.method == 'POST':
        try:
            form = newExp(request.POST)
            if form.is_valid():
                exp = form.save(commit=False)
                
                exp.author = request.user.student
                exp.save()

                return redirect('interview')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'interviewExperience/newInterview.html', context)
