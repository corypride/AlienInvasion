# This site was created by Cory 'CP' Pride in 2022
# Many of the notes used pertaining to the pygame module have been parphrased from the pygame documentation and the Python Crash Course book by Eric Matthes. The directions are also written assuming that the user has at least a basic understanding of python.

import sys
import pygame

class pygameWindowIntro:
    """Overall class to show users how to..."""
    def __init__(self):
        """Initialize game and create some game stuff"""
        # First you must initialize the pygame module
        pygame.init() #see /pygame.html#pygame.init for more info

        # use set_mode to create a display window which will be used as our canvas to draw all the game stuff on

        # we choose the width and height that we want and use these values to pass as the size argument to the set_mode() function
        self.screenWidth = 1200
        self.screenHeight = 800

        # set_mode takes several arguments but the first and most relevant to our introduction to the pygame module is the size parameter which takes a tuple(int, int) which defines the width and height of the game window 
        self.screen = pygame.display.set_mode(size=(self.screenWidth,self.screenHeight)) #see /display.html#pygame.display.set_mode for more info

        # set the caption that will go on the top of the window you created
        pygame.display.set_caption("My Game Name goes Here") #see /display.html#pygame.display.set_caption for more info


    def run_game(self):
        """Start the main loop for your game"""
        while True:

            # pygame.event is a module for interacting with events.Pygame handles all its event messaging through an event queue. To access the queued events we use the method pygame.event.get(). The get() method gets and removes all of the messages from the queue and returns them as a list 

            # You need to constantly look for keyboard and mouse events in order to control and manipulate the things that go on in your game. That includes things like moving your objects or as you see below, looking for an event which allows a user to quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() # Exits the python interpreter

            # Makes the most recently drawn screen visisble
            pygame.display.flip() # see display.html#pygame.display.flip for more info

if __name__ == '__main__':
    # Make an instance of the game and then run it
    ai = pygameWindowIntro()
    ai.run_game()