from django.http import HttpResponse


# Custom http response class for unautherised
class HttpResponseUnauthorized(HttpResponse):
    status_code = 401



