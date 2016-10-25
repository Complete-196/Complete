import uuid

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, DateTimeInput
from django import forms


class Tasks(models.Model):
    user = models.ForeignKey(User)
    uniqueId=models.CharField(max_length=100, default=uuid.uuid4)
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

