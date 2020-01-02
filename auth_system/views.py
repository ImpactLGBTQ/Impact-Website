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
from django.http import response
from .forms import LoginForm, CreateAccForm
from .models import User, AuthTokens
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.urls import reverse_lazy


# Create your views here.

# Handler for the member portal
class LoginPortal(LoginView):
    authentication_form = LoginForm
    template_name = 'auth_system/login_portal.html'


## Handles requests for the create account page
class CreateAccView(View):
    template_name = 'auth_system/create_acc_portal.html'
    form_class = CreateAccForm

    ## Post handler
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Only proceed if the form is valid
            # Get the data out of the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_token = form.cleaned_data['auth_token']

            token = AuthTokens.objects.get(human_readable_tkn__exact=auth_token)
            if token:
                # If the token is valid, aka exists in the lookup table
                user = User.objects.create_user(username=username, password=password, is_impact=True)
                # Delete the old token
                token.delete()
                # Log the user in
                login(request, user)
                # Redirect to the login page
                return response.HttpResponseRedirect(reverse_lazy('auth_system-login_portal'))
            # Return an error
            form.add_error(None, "Token is invalid. Ensure you entered it correctly and try again")
            return render(request, self.template_name, {'form': form})

    ## Get handler
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
