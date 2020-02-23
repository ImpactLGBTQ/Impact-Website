from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from auth_system.forms import LoginForm
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django import http
import json
import logging
from.responses import HttpResponseUnauthorized
# Create your views here.

class GetUserData(View):

    def get(self, request):
       pass


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


