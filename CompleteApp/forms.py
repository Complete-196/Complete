
import re
from django import forms
from django.utils.translation import ugettext_lazy as _
#(\w+\s\w+)
class NewEventForm(forms.Form):

    title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Title"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    duration = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_('Duration'),error_messages={
        'invalid': _("This value must contain only letters, numbers and underscores.")})
    #due = forms.DateField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Due"))