from django.shortcuts import render

# Create your views here.


# Handles request for the homepage
def homepage(request):
    return render(request, 'impact_website/homepage.html')