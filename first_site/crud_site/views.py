from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "crud/crud.html")


def dunbar(request):
    return HttpResponse("hey Dunbar")

def greet(request, name):
    return render(request, "crud/greet.html", {
        "name": name.capitalize()
    })