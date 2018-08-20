import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	num = random.randint(0, 1000)
	some_list = [random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)]
	context = {
		"html_var": "HTML content", 
		"bool_item": True, 
		"num": num, 
		"some_list": some_list
	}
	return render(request, "home.html", context)

def home2(request):
	some_list = [random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000)]
	context = {
	}
	return render(request, "home2.html", context)

def home3(request):
	context = {
	}
	return render(request, "home3.html", context)