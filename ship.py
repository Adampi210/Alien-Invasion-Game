# This program will draw the ship on the screen
import pygame as pg # First I import the pygame module
from pygame.sprite import Sprite

class Ship(Sprite): # Then I create a class Ship
    def __init__(self, game): # and define method init, where I define some attributes
        ###### Format Screen ######

        super().__init__() # This will allow to make groups of ships
        self.screen = game.screen # firtst I get the screen attribute from the game class so that I can access the screen of my game
        self.screen_rect = game.screen.get_rect() # then I create attribute screen_rect using the get_rect() function
        # This function stands for get rectangle, and gives me a rectangle
        # That is because python can treat objects like rectangles, which makes it easier to code their interaction
        # get_rect here returns a rectangle starting at point (0,0) (same as screen), and with width and height of the screen
        # I need this information so that I can place the ship on that rectangle that is currently the screen
        # I later use it to place the starship in a correct location
        self.settings = game.settings # I also import the settings to the ship class, will be needed later

        ###### Format Starship ######

        self.image = pg.image.load('C:/Users/adampi/Desktop/MOJE/programowanie/Python/Alien Invasion Game/images/Starship.bmp') # Firs I define attribute self.image, and load the image of my starship there
        self.rect = self.image.get_rect() # Then I define attribute self.rect, which this time stores the rectangle info of the image imported
        # In other word this als currently has a point (0, 0) as location, and the width and height of he image imported
        self.rect.midbottom = self.screen_rect.midbottom # Here I use the screen rectangle to move the image to the mid bottom of the screen
        # I specifically allign the mid bottom of the image with the mid bottom of the screen
        # This way the image is ideally in the center bottom of the screen at the beggining

        self.moving_right = False # I also state that the ship is initially in rest
        self.moving_left = False # The ship is at rest at every direction
        self.moving_up = False
        self.moving_down = False

        self.ship_speed = game.settings.ship_speed


    def update(self): # This method updates the position of the ship
        if self.moving_right: # If given attribute is set to true, the ship moves in that direction
            self.rect.x += self.ship_speed
        if self.moving_left:
            self.rect.x -= self.ship_speed
        if self.moving_up:
            self.rect.y -= self.ship_speed
        if self.moving_down:
            self.rect.y += self.ship_speed
        self.constraint_ship() # I also constraint where the ship can go

    def constraint_ship(self): # This method defines constraints for the ship so that it doesn't fly off the screen
        if self.rect.x >= self.screen.get_width() - self.image.get_width(): # Here I specify max values in x axis
            self.rect.x = self.screen.get_width() - self.image.get_width()
        elif self.rect.x <= 0:
            self.rect.x = 0

        if self.rect.y <= 0: # and here in y axis
            self.rect.y = 0
        elif self.rect.y >=  self.screen.get_height() - self.image.get_height():
            self.rect.y = self.screen.get_height() - self.image.get_height()

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self): # Then I define a blitme method. It uses blit function
        self.screen.blit(self.image, self.rect) # What it does it basically paints the image over the rectangle that symbolizes the starship
        # Without it I wouldnt see the image of the starship that I imported
