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

from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import LoginForm, CreateAccountForm
from .models import UserModel


# Create your views here.

# Handler for the login portal
def login_portal(request):
    if request.method == 'POST':
        # If its a complete member login, so a post request
        form = LoginForm(request.POST)
        if form.is_valid():
            # Only proceed if the form is valid
            # Get the data out of the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

    else:
        form = LoginForm()
        return render(request, 'auth_system/login_portal.html', {'login_form': form})


# Handler for the 'Create account' page
def create_account(request):
    if request.method == 'POST':
        # If its a post request, so a submitted form
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            # Continue if the form is valid
            # Get the data out of the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            # Create the data models
            user = User(username=username, password=password)
            user_model = UserModel(email=email, user=user)

            # Insert the data into the database
            user.save()
            user_model.save()
    else:
        # If its a request for a signup
        # Create a new form and send it to the html
        form = CreateAccountForm()
        return render(request, 'auth_system/create_account.html', {'create_account_form': form})
