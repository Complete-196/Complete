
from django.shortcuts import render

# Create your views here.
# views.py
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from CompleteApp import views



@csrf_protect
def register(request):

    if request.method == 'POST':
        form1 = RegistrationForm(request.POST)
        if form1.is_valid():
            user = User.objects.create_user(
                username=form1.cleaned_data['username'],
                password=form1.cleaned_data['password1'],
                email=form1.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
        else:
            print form1.errors.values
    else:
        form1 = RegistrationForm()

    return render(request, 'registration/login.html', {'form1':form1})



def register_success(request):
    return render_to_response(
        'registration/success.html',
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')



@login_required
def home(request):
    return views.index(request)