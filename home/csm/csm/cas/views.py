from django.shortcuts import render
from django.http import HttpResponse

def login(request):
	return HttpResponse("Log in")

def logout(request):
	return HttpResponse("Logged out")

