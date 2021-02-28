from .models import Question, Response
from django import forms



class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'autofocus': True,
                'placeholder': 'Ask your Question?'
            })
        }

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'What are your thoughts?'
            })
        }