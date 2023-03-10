from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ship(models.Model):
    """Ship for alien invasion"""
    ship_id = models.AutoField(primary_key=True,auto_created=True,unique=True)
    ship_name = models.CharField(max_length=200,null=False,unique=True)
    ship_displayName = models.CharField(max_length=200,null=False)
    ship_colors = models.CharField(max_length=100,null=False)
    ship_description = models.TextField(max_length=500,null=False)

    def __str__(self):
        """String representation of the ship model"""
        
        if len(self.ship_description) > 50:
            desc_str = f"{self.ship_description[:50]}..."
        else:
            desc_str = self.ship_description

        return  f"ID: {self.ship_id}, Name: {self.ship_name}, Colors: {self.ship_colors}, Desc: " + desc_str
  
class Battlesite(models.Model):
    """Battle site for alien invasion"""
    site_id = models.AutoField(primary_key=True,auto_created=True,unique=True)
    site_name = models.CharField(max_length=200, null=False, unique=True)
    site_displayName = models.CharField(max_length=200, null=False)
    site_description = models.TextField(max_length=500, null=False)

    def __str__(self):
        """String representation of the site model"""
        if len(self.site_description) > 50:
            desc_str = f"{self.site_description[:50]}..."
        else:
            desc_str = self.site_description
        
        return f"ID: {self.site_id}, Site Name: {self.site_name}, Desc: " + desc_str

class Bullet(models.Model):
    """Bullet for alien invasion"""
    bullet_id = models.AutoField(primary_key=True,auto_created=True,unique=True)
    bullet_name = models.CharField(max_length=200,null=False,unique=True)
    bullet_displayName = models.CharField(max_length=200,null=False)
    bullet_description = models.TextField(max_length=500,null=False)

    def __str__(self):
        """String representation of the bullet model"""
        
        if len(self.bullet_description) > 50:
            desc_str = f"{self.bullet_description[:50]}..."
        else:
            desc_str = self.bullet_description

        return  f"ID: {self.bullet_id}, Name: {self.bullet_name}, Desc: " + desc_str

class Invader(models.Model):
    """Invader for alien invasion"""
    invader_id = models.AutoField(primary_key=True,unique=True,auto_created=True)
    invader_name = models.CharField(max_length=200,null=False,unique=True)
    invader_displayName = models.CharField(max_length=200,null=False)
    invader_description = models.TextField(max_length=500,null=False)

    def __str__(self):
        """String representation of the invader model"""
        
        if len(self.invader_description) > 50:
            desc_str = f"{self.invader_description[:50]}..."
        else:
            desc_str = self.invader_description

        return  f"ID: {self.invader_id}, Name: {self.invader_name}, Desc: " + desc_str

class Score(models.Model):
    """Model to hold scores from alien invasion"""
    score_id = models.AutoField(primary_key=True,unique=True,auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    highScore = models.IntegerField(default=0,null=False)
    lastLevel = models.IntegerField(default=1,null=False)
    gameDate = models.CharField(max_length=10,null=False)
    gameTime = models.CharField(max_length=8,null=False)

    def __str__(self):
        """String representation of a Players Score"""
        theString = f"User Name: {self.user}, Last Level Played: {self.lastLevel}, High Score: {self.highScore}"
        return theString


# TODO: Make a helper function that will update/populate the ship, background, alien, and bullet tables with the imageName of the objects from the file. Will need to do a check to be sure that the item is not already in the database before it saves an item. Think about how you will match the item that the user chooses from the site with the dynamically generated lists of the ai_game

