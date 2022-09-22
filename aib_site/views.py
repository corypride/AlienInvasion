import json
from django.shortcuts import render, redirect
from django import forms

from .models import Ship
from .models import Battlesite
# from .forms import ShipForm

# Create your views here.
def index(request):
    """The home page for Alien Invasion Build."""
    return render(request,'aib_site/index.html')

def all_ships(request):
    """This page displays all the ships options for Alien Invasion Build."""
    # May eventually change this to show all components
    ships = Ship.objects.all()
    context = {"ships":ships}
    return render(request,'aib_site/all_ships.html',context)

def ship_form(request):
    """This page displays a form that allows users to select the ship they want to use in a customized version of Alien Invasion."""
    if request.method == 'POST':
    # POST data submitted; process data
    # data will be stored in a json file to be retrieved later and used for the customized alien invasion game
    # print("test")
        filenameAndPath = "aib_site/static/aib_site/json/shipChoice.json"
        with open (filenameAndPath,"w") as f:
			#change this to store the shipname and the file type example (ship.png)		
            ship_name = {"ship_name":request.POST["ship_name"]}
            json.dump(ship_name,f)
            f.close()
            # eventually there will be another page to show the addition of the ship of your choosing to code. And there will be an explanation to go with it
            return redirect("aib_site:all_ships")

    # No data submitted; display the Choose form
    ships = Ship.objects.all()
    context = {"ships":ships}
    return render(request,'aib_site/pick_ship.html',context)

def battlesite_form(request):
    """This page displays a form that allows users to select the Battle site they want to use in a customized version of Alien Invasion."""


    if request.method == 'POST':
        # POST data submitted; process data
        # data will be stored in a json file to be retrieved later and used for the customized alien invasion game
        # print("test")
        filenameAndPath = "aib_site/static/aib_site/json/siteChoice.json"
        with open (filenameAndPath,"w") as f:
			#change this to store the shipname and the file type example (ship.png)		
            site_name = {"site_name":request.POST["site_name"]}
            json.dump(site_name,f)
            f.close()
            # eventually there will be another page to show the addition of the site of your choosing to code. And there will be an explanation to go with it Or... This will go to the next page to choose the next game option
            return redirect("aib_site:all_sites")


    sites = Battlesite.objects.all()
    context = {"sites":sites}
    return render(request,'aib_site/pick_battlesite.html',context)




