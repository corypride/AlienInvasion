import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django import forms
import django.utils.html as test

# for converting the json objects and running the pygame in the terminal
from .static.aib_site.py_code.alien_invasion.communication import getGameSettingsFromJson
import subprocess
# ________________________________

from .models import Ship
from .models import Battlesite
from .models import Bullet
from .models import Invader
from .models import Score
from django.contrib.auth.models import User
from .score import getScoreFromJSON



# Create your views here.

def index(request):
    theStr = str(request.user.id)+" " +str(request.user.username)
    print(theStr)    
    """The home page for Alien Invasion Build."""
    return render(request,'aib_site/index.html')


def all_invaders(request):
    """This page displays all the invader options for Alien Invasion Build."""
    invaders = Invader.objects.all()
    context = {"invaders":invaders, "pgName":'All Invaders'}
    return render(request,'aib_site/all.html',context)

@login_required
def invader_form(request):
    """This page displays a form that allows users to select the ship they want to use in a customized version of Alien Invasion."""
    if request.method == 'POST':
    # POST data submitted; process data
    # data will be stored in a json file to be retrieved later and used for the customized alien invasion game    
        
        filenameAndPath = "aib_site/static/aib_site/json/invaderChoice.json"
        with open (filenameAndPath,"w") as f:
			#change this to store the shipname and the file type example (ship.png)		
            invader_name = {"invader_name":request.POST["invader_name"]}
            json.dump(invader_name,f)
            f.close()
            # eventually there will be another page to show the addition of the ship of your choosing to code. And there will be an explanation to go with it
            return redirect("aib_site:bullet_form")
           
             

    # No data submitted; display the Choose form
    invaders = Invader.objects.all()
    context = {"invaders":invaders}
    return render(request,'aib_site/pick_invader.html',context)


def all_ships(request):
    """This page displays all the ships options for Alien Invasion Build."""
    ships = Ship.objects.all()
    context = {"ships":ships, "pgName":'All Sites'}
    return render(request,'aib_site/all.html',context)

@login_required
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
            return redirect("aib_site:invader_form")
            
            

    # No data submitted; display the Choose form
    ships = Ship.objects.all()
    context = {"ships":ships}
    return render(request,'aib_site/pick_ship.html',context)

def all_sites(request):
    """This page displays all the site options for Alien Invasion Build."""
    # May eventually change this to show all components
    sites = Battlesite.objects.all()
    context = {"sites":sites, "pgName":'All Sites'}
    return render(request,'aib_site/all.html',context)

@login_required
def battlesite_form(request):
    """This page displays a form that allows users to select the Battle site they want to use in a customized version of Alien Invasion."""

    if request.method == 'POST':
        # POST data submitted; process data
        # data will be stored in a json file to be retrieved later and used for the customized alien invasion game
        
        # this is how to import the user model 'from django.contrib.auth.models import User'. This is how to get the user from the request 'request.user.id' and this is how I get a user from the DB User.objects.get(id= 1)

        filenameAndPath = "aib_site/static/aib_site/json/site_and_screen_choice.json"
        with open (filenameAndPath,"w") as f:
			#change this to store the shipname and the file type example (ship.png)		
            site_name = {"screen_width":request.POST["screen_width"],"screen_height":request.POST["screen_height"],"site_name":request.POST["site_name"]}
            json.dump(site_name,f)
            f.close()
            # eventually there will be another page to show the addition of the site of your choosing to code. And there will be an explanation to go with it Or... This will go to the next page to choose the next game option
            return redirect("aib_site:ship_form")
           


    sites = Battlesite.objects.all()
    context = {"sites":sites}
    return render(request,'aib_site/pick_battlesite.html',context)

def all_bullets(request):
    """This page displays all the ships options for Alien Invasion Build."""
    bullets = Bullet.objects.all()
    context = {"bullets":bullets}
    return render(request,'aib_site/all.html',context)

@login_required
def bullet_form(request):
    """This page displays a form that allows users to select the bullets they want to use in a customized version of Alien Invasion."""
    if request.method == 'POST':
    # POST data submitted; process data
    # data will be stored in a json file to be retrieved later and used for the customized alien invasion game
    # print("test")
        filenameAndPath = "aib_site/static/aib_site/json/bulletChoiceUserId.json"
        with open (filenameAndPath,"w") as f:
			#change this to store the shipname and the file type example (ship.png)		
            bullets = {"bullet1Name":request.POST["bulletName1"],"userId":request.user.id,}
            json.dump(bullets,f)
            f.close()
            # eventually there will be another page to show the addition of the ship of your choosing to code. And there will be an explanation to go with it
            return redirect("aib_site:play_game")

    # No data submitted; display the Choose form
    bullets = Bullet.objects.all()
    print(bullets)
    context = {'bullets':bullets}
    return render(request,'aib_site/pick_bullets.html',context)

@login_required
def saveScore(request):
    """Save score after a game"""
    dictObj = getScoreFromJSON()
    
    if dictObj["highScore"] > 0:
        userId = int(dictObj["userId"])

        user = User.objects.get(id=userId)
        hs = dictObj["highScore"]
        ll = dictObj["lastLevel"]
        gd = dictObj["todaysDate"]
        gt = dictObj["endTime"]

        s = Score(user= user,highScore= hs,lastLevel= ll,gameDate= gd,gameTime= gt)
        s.save(force_insert=True)
    return redirect("aib_site:high_scores")
    

def highScores(request):
    """Display a List of the top ten High Scores"""
    scores = Score.objects.order_by("-highScore")[0:10]

    # add a ranking to the collection so it can be displayed in the table
    i = 1
    temp = {}
    for score in scores:
        temp[i] = {"rank":i,"score":score}
        
        i+=1

    context = {"scores":temp,"highScore":True}
    return render(request,'aib_site/highScores.html',context)


@login_required
def continueWithSameSettings(request):
    """Play alien invasion again with the previous settings"""
    commandLineString = getGameSettingsFromJson()
    subprocess.run(commandLineString)
    return redirect("aib_site:save_score")


@login_required
def playGame(request):
    """Display all the players choices and a play button to start the game"""
    commandLineString = getGameSettingsFromJson()

    # TODO: on the submit button of this form i need to put the saveScore() also I need to modify that method to check if the info is already saved before it saves it again

    if request.method == 'POST' and request.POST["willPlay"]:
        subprocess.run(commandLineString)
        return redirect("aib_site:save_score")

    # otherwise render the page with all the users choices (this requires all the filepaths to the choices)
    
    # get the slice of the commandLineString that has the player's options
    settingList = getGameSettingsFromJson()[2:]
    # print(settingList)
    context = {}
    context.update(width=settingList[0])
    context.update(height=settingList[1])
    context.update(siteName=settingList[2])
    context.update(shipName=settingList[3])
    context.update(invaderName=settingList[4])
    context.update(bulletName=settingList[5])

    return render(request,"aib_site/play.html",context)

def displayPygameIntro(request):
    """Displays pygame module definitions"""
    
    mystr = test.format_html(test.mark_safe('static aib_site/py_code/pygame/docs/generated/ref/pygame.html?highlight=pygame init#pygame.init'))  
   
    context = {"intro":True,"test":mystr}
    return render(request, "aib_site/pygame_intro.html",context)
        

