from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

@login_required
def index(request):
    return render_to_response("index.html",
                               {"user" : request.user,
                               "HelloHello" : "Hello World - Django"})