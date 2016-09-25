from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	#return HttpResponse("Hello, welcome to the unofficial uWaterloo coop"
	#	"sequence matcher webapp!")
	return render(request,'matcher/index.html',{})

def choose(request):
	return HttpResponse("Choose your sequence here!")

def thanks(request):
	return HttpResponse("Response here!")