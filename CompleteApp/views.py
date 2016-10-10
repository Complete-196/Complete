from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from CompleteApp.users import Tasks


@login_required
def index(request):
    query_results = Tasks.objects.filter(user=request.user)#values_list('title', flat='True')
    print request.user
    return render_to_response("index.html",
                               {"query_results" : query_results, 'user':request.user})

@login_required
def addview(request):
    if request.method == 'POST':
            form = request.POST
            model = Tasks(
                user=request.user,
                title= form.get('title'),
                dueTime= form.get('due'),
                duration= form.get('duration'),
            )
            model.save()
            return HttpResponseRedirect('/CompleteApp')

    return render(request, 'newEvent.html')

