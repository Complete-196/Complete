
import re
from django import forms
from django.utils.translation import ugettext_lazy as _
#(\w+\s\w+)
class NewEventForm(forms.Form):

    title = forms.RegexField(regex=r'$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
                                label=_("Title"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    # duration = forms.RegexField(regex=r'[0-9.]+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)),
    #                             label=_('Duration'),error_messages={
    #     'invalid': _("This value must contain only letters, numbers and underscores.")})
    #
class RegistrationForm(forms.Form):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=_("Password (again)"))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data