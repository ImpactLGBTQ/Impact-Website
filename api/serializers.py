from rest_framework import serializers
from auth_system.models import User
from posting import models as post_models


# Serializes the User to be sent back
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'uuid',
        )


# Serializes a post to be send as json in response to a rest api hit
class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = post_models.Post
        fields = (
            'title',
            'content',
            'author_name',
            'uuid',
            'author',
        )

    def get_author_name(self, post):
        username = post.author.username
        return username

