from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'Contact.html')

def add(request):
    return HttpResponse('Hello This is a Form  Page')