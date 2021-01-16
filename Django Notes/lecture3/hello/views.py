from django.shortcuts import render

from django.http import HttpResponse #Import HttpResponse library from django.http

# Create your views here.


#- The index of the hello application
def index(request):
    return render(request, "hello/index.html") # This function can receive a html template. hello/templates/hello/index.html

def bran(request):
    return HttpResponse("Hello, Bran") 

def dan(request):
    return HttpResponse("Hello, Dan")

# Automatic url function, receiving a name and returning it
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")

# Automatic url function, receive a name and send it to the html template
def greet2(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize(), #sending name to the template

    })