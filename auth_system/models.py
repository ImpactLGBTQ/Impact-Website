from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.

class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)

    access_level = models.IntegerField(default=1, null=False)
