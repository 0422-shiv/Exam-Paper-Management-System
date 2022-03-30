from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext_lazy as _

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control password_change", 'type':"Password", 'placeholder': _("Old Password")}), localize=True)
    new_password1 = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control password_change", 'type':"Password", 'placeholder': _("New Password")}), localize=True)
    new_password2 = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control password_change", 'type':"Password", 'placeholder': _("Confirm Password")}), localize=True)