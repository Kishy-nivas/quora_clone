from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

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