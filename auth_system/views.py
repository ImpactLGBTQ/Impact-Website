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
from .forms import LoginForm
# Create your views here.

# Handler for the member portal
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