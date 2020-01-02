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
from .forms import LoginForm, CreateAccForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import View


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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_token = form.cleaned_data['auth_token']



    ## Get handler
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


    def check_token(self, token: str):
        pass