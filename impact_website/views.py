from django.shortcuts import render


# Create your views here.


# Handles request for the homepage
def homepage(request):
    return render(request, 'impact_website/homepage.html')


# Handles request for the 'about us' page
def about_us(request):
    return render(request, 'impact_website/who_are_we.html')


# Handles request for the 'signposting' page
def signposting(request):
    return render(request, 'impact_website/signposting.html')
