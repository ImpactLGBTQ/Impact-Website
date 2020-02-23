from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'api'
urlpatterns = (
    path('auth/logmein/', views.AuthenticateUser.as_view(), name='authenticate-user'),

)

