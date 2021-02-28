from django.shortcuts import render
from .models import interviewExp

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    context = {
        'interviewExp':interviewExp.objects.all()
    }

    return render(request,'interviewExperience/index.html',context)