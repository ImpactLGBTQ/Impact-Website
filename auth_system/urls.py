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

from django import urls
from django.urls import path
from . import views
# File for urls for the auth_system app

urlpatterns = (
    path('login', views.LoginPortal.as_view(), name='auth_system-login_portal'),
    path('create-account', views.CreateAccView.as_view(), name='auth_system-create-account-portal'),
    path('profile/<str:user_id>', views.ProfileView.as_view(), name='auth_system-view-profile'),
    path('logout', views.LogoutUser.as_view(), name='auth_system-logout'),
)