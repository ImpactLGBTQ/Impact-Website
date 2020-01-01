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
from django.db import models
from django import forms


# Forms file for the auth_system app

## Login form presented to the user when they want to (or are required to) login
class LoginForm(forms.Form):
    ## Username field - Required
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ## Password field - Required
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    ## Remember me field - Not required
    remember_me = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input custom-control-input'}))


## Create an account form presented to the user when they wish to create an account
class CreateAccForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # Auth token required to get an account. May change in future
    auth_token = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
