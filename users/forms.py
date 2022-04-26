from django.forms import ModelForm, widgets
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column
from crispy_forms.bootstrap import InlineCheckboxes, FormActions
from django.utils.translation import ugettext_lazy as _
import datetime as dt
from django.urls import reverse
from django.contrib.auth.forms import *
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class UpdateUserForm(UserChangeForm):
    username = forms.CharField(max_length=140, label="Username*")
    class Meta:
        model = User
        fields = ('username',)

class UpdatePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Old Password*")
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, label="New Password*")
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label="Re-type New Password*")
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        