from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

def index(request,):
    return render_to_response("index.html",
                               {"Testing" : "Django Template Inheritance ",
                               "HelloHello" : "Hello World - Django"})