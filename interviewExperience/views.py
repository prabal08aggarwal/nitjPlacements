from django.shortcuts import render,redirect
from .models import interviewExp

from django.contrib.auth.decorators import login_required

from .forms import newExp
# Create your views here.

@login_required
def index(request):
    context = {
        'interviewExp':interviewExp.objects.all()
    }

    return render(request,'interviewExperience/index.html',context)


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
