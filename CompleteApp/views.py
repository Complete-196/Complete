
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from CompleteApp.users import Tasks, TasksForm
from CompleteApp.forms import *


@login_required
def index(request):
    query_results = Tasks.objects.filter(user=request.user)#values_list('title', flat='True')
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
                    duration= form.cleaned_data['duration'],
                )
                model.save()
                return HttpResponseRedirect('/CompleteApp')
            else:
                print form.errors
    else:
        form = NewEventForm()

    return render(request, 'newEvent.html', {'form': form})
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


