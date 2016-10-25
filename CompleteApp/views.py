import time
import sys
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from CompleteApp.users import Tasks, TasksForm
from CompleteApp.forms import *


@login_required
def index(request):

    query_results =  organizer(list(Tasks.objects.filter(user_id=request.user).order_by('dueTime')))
    return render_to_response("index.html",
                               {"query_results" : query_results, 'user':request.user})

@login_required
def addview(request):
    if request.method == 'POST':
            form = NewEventForm(request.POST)
            if form.is_valid():
                model = Tasks(
                    user=request.user,
                    title= form.cleaned_data['title'],
                    dueTime= request.POST.get('due'),
                    duration= duration(request.POST.get('Days'), request.POST.get('Hours'),request.POST.get("Minutes"))#form.cleaned_data['duration'],
                )
                model.save()
                return HttpResponseRedirect('/CompleteApp')
            else:
                print form.errors
    else:
        form = NewEventForm()

    return render(request, 'newEvent.html', {'form': form})

def duration(days, hours, minutes):
    if len(days)<1:
        days = 0
    if len(hours)<1:
        hours = 0
    if len(minutes)<1:
        minutes=0
    days = 1+int(days)
    if days < 10:
        days= '0'+str(days)
    if int(hours) < 10:
        hours = '0'+ hours
    if int(minutes) < 10:
        minutes = '0'+minutes
    return str(days)+' '+hours+':'+minutes

@login_required
def delete(request,id):
    server = Tasks.objects.get(uniqueId=id).delete()
    return HttpResponseRedirect('/CompleteApp')

@login_required()
def edit(request,id):
    event = Tasks.objects.get(uniqueId=id)
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        if form.is_valid():
            form = TasksForm(form, instance=event)
            model = Tasks(
                user = Tasks.objects.get(uniqueId=id).user,
                title = request.POST.get('title'),
                dueTime = request.POST.get('dueTime'),
                duration = request.POST.get('duration'),
            )
            event.delete()
            model.save()
            return HttpResponseRedirect('/CompleteApp')
    else:
        form = TasksForm(instance=event)

    return render(request, 'editForm.html', {'form': form})

'''
def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
'''



def toEpoch(date):
    if len(date) < 19:
        pattern = '%Y-%m-%d %H:%M'
    else:
        pattern = '%Y-%m-%d %H:%M:%S'
    return int(time.mktime(time.strptime(date, pattern)))

def deadline(due, duration):

    base = time.strftime('%Y-%m-', time.localtime(0))
    duration = base + duration
    epochDuration = toEpoch(duration)
    epochDue = toEpoch(due)
    deadline = epochDue-epochDuration
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(deadline))


def organizer(a):
    x = sys.maxint
    for k in reversed(a):
        i = str(k.dueTime)[:16]
        j = str(k.duration)[:16]
        if toEpoch(i) > x:
            i = time.strftime('%Y-%m-%d %H:%M', time.localtime(x))
        k.dueTime = deadline(i,j)

        x = toEpoch(deadline(i, j))
    return a
