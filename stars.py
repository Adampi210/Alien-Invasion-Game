import pygame as pg # I import modules
from pygame.sprite import Sprite
import random as r

class Star(Sprite): # and create a Star class that uses Sprite class as its parent class
    def __init__(self, game):
        super().__init__() # I initiate it as Sprite

        self.screen = game.screen # And add some basic attributes, screen, settings, and color
        self.settings = game.settings
        self.color = pg.Color(255, 255, 255)
        self.rect = pg.Rect(r.randint(0, game.settings.screen_width), r.randint(0, game.settings.screen_height), 1, 1) # Then I randomly choose its position on the screen

    def draw_star(self): # Finally I create a star method that draws the star on the screen
        pg.draw.rect(self.screen, self.color, self.rect)
