from django.shortcuts import render
from .models import Ship

# Create your views here.
def index(request):
    """The home page for Alien Invasion Build."""
    return render(request,'aib_site/index.html')

def all_ships(request):
    """This page displays all the ships options for Alien Invasion Build."""
    # May eventually change this to show all components
    return render(request,'aib_site/all_ships.html')

def ship_form(request):
    """This page displays a form that allows users to select the ship they want to use in a customized version of Alien Invasion."""
    ships = Ship.objects.all()
    context = {"ships":ships}
    return render(request,'aib_site/ship_form.html',context)