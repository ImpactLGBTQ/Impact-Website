from django.contrib.auth.views import LogoutView
from django.core.cache import cache
from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
import posting.models as posting_models
from .serializers import UserSerializer, PostSerializer
from rest_framework import permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django import http
import json
import logging
from.responses import HttpResponseUnauthorized
# Create your views here.


class AuthenticateUser(ObtainAuthToken):
    def post(self, request, **kwargs):
        json_data = request.body
        print("Recived: ", json_data)

        try:
            data = json.loads(json_data)
        except TypeError:
            logging.debug("Failed to decode json data. RAW: {}".format(json_data))
            return http.HttpResponseBadRequest()

        # Data has been parsed successfully

        # Unpack the data
        username = data['username']
        password = data['password']

        # Test login
        user = authenticate(username=username, password=password)

        if user:
            # Logged in successfully
            # Get the token
            token = Token.objects.get(user=user)
            return http.JsonResponse({"token": token.key})

        return HttpResponseUnauthorized()


class GetPosts(APIView):

    def get(self, request, num):
        # Ensure not too big
        if num < 1 or num > 20:
            return http.HttpResponseBadRequest()

        if request.user.is_anonymous:
            # If its an annoymous user, aka not logged in person, set the default 0 access level
            access_level = 0
        else:
            # Else use the users access level
            # Ensure access level is updated
            request.user.sync_access_level()
            access_level = request.user.access_level
        cache_query = 'whats_on_recent-{}'.format(access_level)
        # Check the cache for these posts
        cached_posts = cache.get(cache_query)
        if cached_posts:
            posts = cached_posts
            logging.info('Hitting cache for Whats on posts at access level {}'.format(access_level))
        else:
            # Pull first 10 posts
            posts = posting_models.Post.objects.filter(required_access__lte=access_level,
                                                       post_type__exact=0).order_by()[:10]
            # Cache the posts
            cache.set(cache_query, posts)
            logging.info("Hitting database and adding to cache for Whats on posts at access level {}".format(access_level))

        serialized = PostSerializer(posts, many=True)
        return http.JsonResponse(serialized.data, safe=False)








# Get a csrf token
class GetCSRF(APIView):

    def get(self, request, **kw):
        return render(request, 'api/get_csrf.html')


class GetUserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class DeauthUser(LogoutView, APIView):
    pass
