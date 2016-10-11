from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    dueTime = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)

