from django.shortcuts import render
from django.views import View
from auth_system.forms import LoginForm
from django.contrib.auth import authenticate
from django import http
import json
import logging
# Create your views here.

class GetUserData(View):

    def get(self, request):
       pass


class AuthenticateUser(View):

    def post(self, request):
        json_data = request.body

        try:
            data = json.loads(json_data)
        except TypeError:
            logging.debug("Failed to decode json data. RAW: {}".format(json_data))
            return http.HttpResponseBadRequest()

        # Data has been parsed successfully

        # Unpack the data
        username = data['username']
        password = data['password']
        print(username)
        print(password)
        return http.HttpResponse()



