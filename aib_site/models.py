from django.db import models

# Create your models here.

class Ship(models.Model):
    """Ship for alien invasion"""
    ship_id = models.AutoField(primary_key=True,auto_created=True,unique=True)
    ship_name = models.CharField(max_length=200,null=False,unique=True)
    ship_description = models.TextField(max_length=500,null=False)

    def __str__(self):
        """String representation of the ship model"""
        return f"ID: {self.ship_id} Name: {self.ship_name} Desc: {self.ship_description[:75]}..."

# ToDO: duplicate the ship model to make the other models alien ship or aliens, bullets, and backgrounds.

# class GameOptions(models.Model):
#     """Available options for ships, alien ship or aliens, bullets, and backgrounds."""
#     # Once the table is populated it will be used to populate selects on an html page
#     # ships
#     # aliens
#     # alien ships
#     # bullet
#     # backgrounds




# class UserSettings(models.Model):
#     """User specific settings for a game of alien invasion"""
