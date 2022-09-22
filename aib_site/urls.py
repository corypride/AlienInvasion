"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'aib_site'

urlpatterns = [
    # Home page
    path('',views.index, name='index'),
    # Display all Ships
    path('ships/',views.all_ships, name='all_ships'),
    # Choose Ship Form
    path('ships/choose/', views.ship_form, name='ship_form'),
    # Choose a Background Form
    path('battlesites/choose',views.battlesite_form,name='battlesite_form'),
    # Display all Sites
    path('sites/',views.all_sites, name='all_sites'),
    

    # for the path() function - the first arg is a string that helps Django route the current request properly. Django receives the requested URL and tries to route the request to a view. It does this by searching all the URL patterens i've defined to find one that matches the current request. Django ignores the base URL for the project(http://localhost:8000/), so the empty string ('') matches the base URL. Any other URL won't match this pattern, and Django will return an error page if the URL requested does not match any existing URL patterns.

    # The second arg in path() specifies which function to call in views.py. When a requested URL matches the patteren i've defined, Django calls the index() function from views.py

    # The third arg in path() provideds the name index for the URL pattern so we can refer to it in other code sections. Whenever we want to provide a link to the home page, we'll use this name instead of writing out a URL.

]