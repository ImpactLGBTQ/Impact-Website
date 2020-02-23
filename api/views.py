from django.shortcuts import render
from django.views import View
from auth_system.forms import LoginForm
from django.contrib.auth import authenticate
from django import http
import json
import logging
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class GetUserData(View):

    def get(self, request):
       pass


class AuthenticateUser(View):
    @csrf_exempt
    def post(self, request):
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
        print(username)
        print(password)
        return http.HttpResponse()



