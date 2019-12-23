from django.shortcuts import render

# Create your views here.

# Handler for the member portal
def member_portal(request):
    if request.method == 'POST':
        # If its a complete member login, so a post request

    else:
        form =