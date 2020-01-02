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

from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.User)
class UserAccountsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AuthTokens)
class AuthenticationTokensAdmin(admin.ModelAdmin):
    pass
