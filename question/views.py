from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,QuestionForm,AnswerForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views import generic 
from django import forms
from .models import userprofile,Question
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
	help_text=  'Site under construction '
	return render(request,'question/index.html',{'text':help_text})

def signup(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			User.objects.create_user(username =username,password =password, email =email )
			user = authenticate(username = username,password = password )
			login(request,user)
			return redirect('/')
		else :
			return render(request,'registration/signup.html',{'form':form })
	else:
		return render(request,'registration/signup.html',{'form':SignUpForm()})


"""class profileform(forms.ModelForm):
	class Meta:
		model = userprofile
		exclude =('username',)   
"""


class profiledetail(generic.DetailView):
	template_name = "question/profiledetail.html"
	model = userprofile
	context_object_name = 'userprofile'
   
@login_required
def ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question()
            question.user = request.user
            question.title = form.cleaned_data.get('title')
            question.description = form.cleaned_data.get('description')
            question.save()
            tags = form.cleaned_data.get('tags')
            question.create_tags(tags)
            return redirect('/')

        else:
            return render(request, 'question/ask.html', {'form': form})

    else:
        form = QuestionForm()

    return render(request, 'question/ask.html', {'form': form})

class question_list(generic.ListView):
	model = Question
	template_name = "question/questionlist.html"
	context_object_name= "question_list"


@login_required
def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            user = request.user
            answer = Answer()
            answer.user = request.user
            answer.question = form.cleaned_data.get('question')
            answer.description = form.cleaned_data.get('description')
            answer.save()
            return redirect('/')
        else:
            question = form.cleaned_data.get('question')
            return render(request, 'question/question.html', {
                'question': question,
                'form': form
            })
    else:
        return redirect('/')






   
   

