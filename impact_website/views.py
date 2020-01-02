# ==============================================================================
#      Impact group website
#      Copyright (C) 2019  Natasha England-Elbro
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ==============================================================================

from django.shortcuts import render


# Create your views here.


## Handles request for the homepage
# @returns The rendered view of the homepage
def homepage(request):
    return render(request, 'impact_website/homepage.html')


## Handles request for the 'about us' page
def about_us(request):
    return render(request, 'impact_website/who_are_we.html')


## Handles request for the 'signposting' page
def signposting(request):
    return render(request, 'impact_website/signposting.html')


## Handles request for the 'FAQ' page
def faq_page(request):
    return render(request, 'impact_website/FAQ.html')
