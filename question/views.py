from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	help_text=  'Site under construction '
	return render(request,'question/index.html',{'text':help_text})