from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    dueTime = models.CharField(max_length=50)
    duration = models.CharField(max_length=100)

'''
class Taskscheck(forms.Form):
    title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                              label=_("Username"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})

'''