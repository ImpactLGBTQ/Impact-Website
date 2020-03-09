# ==============================================================================
#      Impact group website
#      Copyright (C) 2019  Natasha England-Elbro
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================
from django.contrib.auth import password_validation
from django.db import models
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from .models import User

# Forms file for the auth_system app

## Login form presented to the user when they want to (or are required to) login
class LoginForm(AuthenticationForm):
    ## Username field - Required
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ## Password field - Required
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ## Remember me field - Not required
    remember_me = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={
        'class': 'custom-control-input'}))


## Create an account form presented to the user when they wish to create an account
class CreateAccForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),

    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )

    # Auth token required to get an account. May change in future
    auth_token = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Authentication '
                                                                                                    'Token')
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
