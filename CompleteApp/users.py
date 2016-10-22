from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, DateTimeInput


class Tasks(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    dueTime = models.DateTimeField(max_length=50)
    duration = models.CharField(max_length=100)

class MyDateTimeInput(DateTimeInput):
    input_type = 'datetime'

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'dueTime', 'duration']
        print model.dueTime

