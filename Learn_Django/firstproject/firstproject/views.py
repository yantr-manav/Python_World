from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world! This is my first Django project.")
    return render(request,'index.html')

def about(request):
    return HttpResponse("Hello, world! This is my about page ")


def contact(request):
    return HttpResponse("Hello, world! This is my contact page.")