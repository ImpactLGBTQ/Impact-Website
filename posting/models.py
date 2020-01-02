from django.db import models
from auth_system.models import User
from ImpactWebsite import settings
import uuid


# Create your models here.

class Post(models.Model):
    # Post author
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, unique=False)

    # Post uuid
    uuid = models.UUIDField(default=uuid.uuid4, null=False, primary_key=True)

    # Content and display
    title = models.CharField(max_length=1024, null=False, default="")
    content = models.TextField(null=False, default="")

    # Score
    upvotes = models.IntegerField(null=False, default=0)
    downvotes = models.IntegerField(null=False, default=0)

    # Optional image
    image = models.ImageField(default=None, unique=False)

    # Post types
    POST_TYPES = (
        ('whatson', 'Whats on (Feed post)'),
        ('event', 'Event (Impact post)'),
    )
    post_type = models.CharField(max_length=8, choices=POST_TYPES, null=False, default='whatson')

    # Access levels
    ACCESS_LEVEL_REQUIRED = (
        (0, 'None'),
        (1, 'Member of Impact'),
        (2, 'Staff/Volunteer of Impact'),
    )
    required_access = models.IntegerField(choices=ACCESS_LEVEL_REQUIRED, null=False, default=0)

    # Visibility (turn off instead of deleting, allows historical proof)
    is_visible = models.BooleanField(default=True, null=False, help_text='Visibility, toggle instead of deleting')

    def __str__(self):
        return self.title

