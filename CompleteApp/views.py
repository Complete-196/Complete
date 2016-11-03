import time
import sys
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response


from CompleteApp.users import Tasks, TasksForm
from CompleteApp.forms import *


@login_required
def index(request):

    query_results = organizer(Tasks.objects.filter(user_id=request.user).order_by('dueTime'))
    print query_results
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
        hours = '0'
    if len(minutes)<1:
        minutes= '0'
    days = 1+int(days)
    if days < 10:
        days= '0'+str(days)
    if int(hours) < 10:
        hours = '0'+ hours
    if int(minutes) < 10:
        minutes = '0' + minutes
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
                dueTime = request.POST.get('due'),
                duration = duration(request.POST.get('Days'), request.POST.get('Hours'),request.POST.get("Minutes")),
            )
            event.delete()
            model.save()
            return HttpResponseRedirect('/CompleteApp')
    else:
        form = TasksForm(instance=event)
    day = int(event.duration.split(' ')[0])-1
    hour = int(event.duration.split(' ')[1].split(':')[0])
    minute = int(event.duration.split(' ')[1].split(':')[1])
    event.dueTime=str(event.dueTime).split(' ')[0] + "T" + str(event.dueTime).split(" ")[1].split("+")[0]

    return render(request, 'editForm.html', {"day": day, "hour": hour, "minute":minute,"event" : event,'form': form})

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

def niceString(dedline):
    monthmap = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
                7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    hourfloat = {0:'12',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'10',11:'11',12:'12'}
    minutes = {00:'00',01:'01',02:'02',03:'03',04:'04',05:'05',06:'06',07:'07', 8:'08', 9:'09'}
    return monthmap[dedline.tm_mon] + " " + str(dedline.tm_mday)+ " at " + hourfloat[(dedline.tm_hour)%12] + ":"+ \
           (minutes[dedline.tm_min] if dedline.tm_min<10 else str(dedline.tm_min)) + \
            (" AM" if (dedline.tm_hour)/12 < 1 and dedline.tm_hour/12 !=2 else " PM")

def organizer(a):
    x = sys.maxint
    for k in reversed(a):
        i = str(k.dueTime)[:16]
        j = str(k.duration)[:16]
        if toEpoch(i) > x:
            i = time.strftime('%Y-%m-%d %H:%M', time.localtime(x))
        dedline = time.strptime(deadline(i,j), '%Y-%m-%d %H:%M:%S')
        k.dueTime = niceString(dedline)
        x = toEpoch(deadline(i, j))
    return a
