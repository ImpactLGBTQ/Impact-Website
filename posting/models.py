import logging

from django.db import models
from auth_system.models import User
from ImpactWebsite import settings
import uuid
import datetime


# Create your models here.

class Post(models.Model):
    # Post author
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, unique=False)

    # Post uuid
    uuid = models.UUIDField(default=uuid.uuid4, null=False, primary_key=True)

    # Content and display
    title = models.CharField(max_length=1024, null=False, default="", help_text='Post title')
    content = models.TextField(default="")

    # Score
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    # Optional image
    image = models.ImageField(default=None, unique=False)

    # Post types
    POST_TYPES = (
        (0, 'Whats on (Feed post)'),
        (1, 'Event (Impact post)'),
    )
    post_type = models.IntegerField(choices=POST_TYPES, default=0)

    # Access levels
    ACCESS_LEVEL_REQUIRED = (
        (0, 'Everyone'),
        (1, 'Member of Impact'),
        (2, 'Staff/Volunteer of Impact'),
    )
    required_access = models.IntegerField(choices=ACCESS_LEVEL_REQUIRED, null=False, default=0, blank=False)

    # Visibility (turn off instead of deleting, allows historical proof)
    is_visible = models.BooleanField(default=True, help_text='Visibility, toggle instead of deleting')

    # Post dating
    post_date = models.DateTimeField(default=datetime.datetime.utcnow, null=False)
    last_edit = models.DateTimeField(default=datetime.datetime.utcnow, null=False)

    class Meta:
        ordering = ('post_date', 'last_edit')
