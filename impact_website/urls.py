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

from django import urls
from django.urls import path
from . import views

# urls python file for the impact_forum app


urlpatterns = (
    path('', views.homepage),
    path('home', views.homepage,  name='impact_website-homepage'),
    path('about-us', views.about_us, name='impact_website-about-us'),
    path('signposting', views.signposting, name='impact_website-signposting'),
    path('faq', views.faq_page, name='impact_website-FAQ'),
    path('data-policy', views.data_policy, name='impact_website-data-policy'),
)
