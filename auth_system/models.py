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

from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import secrets


# Create your models here.


def generate_token():
    tkn = secrets.token_hex(6)
    return tkn


## Overrides and extends the base user class
class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    # Access restrictions
    is_impact = models.BooleanField(default=False, null=False)
    is_impact_staff = models.BooleanField(default=False, null=False)
    access_level = models.IntegerField(default=1, null=False)


class AuthTokens(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)

    ## The human readable token used
    human_readable_tkn = models.CharField(default=generate_token, null=False, max_length=12)
