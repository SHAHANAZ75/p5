from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.
def index(request):
    return HttpResponse("<h1> welcome to views of an app</h1>")
def home(request):
    return render(request,"myapp1/home.html",{'name':"shanu"})
def fact(request,n):
    n=int(n)
    return HttpResponse("<h4> factorial is  {}</h4>".format(factorial(n)))
def parent(request):
    return render(request,"myapp1/base.html")
def child(request):
    return render(request,"child.html")
def sam(request):
    return render(request,"myapp1/sam.html")
