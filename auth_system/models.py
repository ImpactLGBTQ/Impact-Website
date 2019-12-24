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

from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.

# User model which extends the build in model and attaches itself to it
class UserModel(models.Model):
    # Internal identifiers
    # User binding to extend built-in user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    # External identifiers (i.e username, email etc)
    email = models.EmailField(default=None)

    # Access restrictions
    is_impact = models.BooleanField(default=False, null=False)
    is_staff = models.BooleanField(default=False, null=False)
    access_level = models.IntegerField(default=1, null=False)

