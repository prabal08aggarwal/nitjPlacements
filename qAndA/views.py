from django.shortcuts import render, redirect
from .forms import NewQuestionForm, NewReplyForm, NewResponseForm, qFilter
from django.contrib.auth.decorators import login_required
from .models import Question, Response
from django.core.paginator import Paginator
# Create your views here.

@login_required
def newQuestionPage(request):
    form = NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                
                question.author = request.user.student
                question.save()

                return redirect('qAindex')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'qAndA/new-question.html', context)

@login_required
def homePage(request):
    form = qFilter
    qs = Question.objects.all().order_by('-created_at')

    title = request.GET.get('title')
    authorName = request.GET.get('author')

    if title is not None and title != '':
        qs = qs.filter(title__icontains = title)

    if authorName is not None and authorName != '':
        qs = qs.filter(author__firstName__icontains = authorName)

    paginator = Paginator(qs,10)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    context = {
        'form':form,
        'questions': page_obj
    }
    return render(request, 'qAndA/homepage.html', context)

@login_required
def questionPage(request, id):
    response_form = NewResponseForm()
    # reply_form = NewReplyForm()

    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user.student
                response.question = Question(id=id)
                response.save()
                #return redirect('questionPage')
                #return redirect('qa/question/'+str(id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    context = {
        'question': question,
        'response_form': response_form,
        # 'reply_form': reply_form,
    }
    return render(request, 'qAndA/question.html', context)


