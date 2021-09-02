import pygame as pg # First I import pygame and sprite
from pygame.sprite import Sprite

class Alien(Sprite): # Then I create an Alien class with Sprite as its parent
    def __init__(self, game): # And I inititate it with the game
        super().__init__() # I give it same attributes as sprite

        self.screen = game.screen # and inititate some others like scree, settings, image, and positions
        self.settings = game.settings

        self.image = pg.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width # Initial position is later changed
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) # This is to track the x position in a more precise way

    def check_edges(self): # This checks if the alien has reached the edge (because they are a group, It checks if fleet has reached the edge)
        screen_rect = self.screen.get_rect() # Firs I need the edge of the screen
        if self.rect.right >= screen_rect.right or self.rect.left <= 0: # And if it has been reached I return True
            return True

    def update(self): # This updates the posiotion of the alien fleet
        self.x += self.settings.alien_speed * self.settings.fleet_direction # It changes the x position accordingly to its speed
        self.rect.x = self.x # Ands sets this position
