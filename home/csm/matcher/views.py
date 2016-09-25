from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

from .forms import StudentForm

def index(request):
	#return HttpResponse("Hello, welcome to the unofficial uWaterloo coop"
	#	"sequence matcher webapp!")
	return render(request,'matcher/index.html',{})

def choose(request):
	form = StudentForm()
	return render(request,'matcher/choose3.html',{"form":form})

def thanks(request):
	return HttpResponse("Response here!")