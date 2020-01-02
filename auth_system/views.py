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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import response
from .forms import LoginForm, CreateAccForm
from .models import User, AuthTokens
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
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
    next = reverse_lazy('auth_system-view-profile', args={'user_id': 'me'})

    ## Post handler
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Only proceed if the form is valid
            # Get the data out of the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
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
            return render(request, self.template_name, {'form': form})
        # If the form is invalid
        form.add_error('password1', 'Password too weak')
        return render(request, self.template_name, {'form': form})
    ## Get handler
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})


## Displays a users profile
class ProfileView(View):
    template = 'auth_system/profile_page.html'

    ## Displays the profile based on their id
    def get(self, request, user_id: str):
        if user_id == 'me':
            # The user profile shortcut to the current user
            user_id = request.user.uuid
        user = User.objects.get(uuid__exact=user_id)
        if user:
            # If its a valid user
            return render(request, self.template, {'users_profile': user})
        else:
            # If its invalid uuid for a user
            return response.Http404()


## Logout view called to log a user out
class LogoutUserView(LogoutView, LoginRequiredMixin):
    next_page = reverse_lazy('impact_website-homepage')

