## This will display the score on the screen

import pygame.font as pgf # I first import the pygame font module
from pygame.sprite import Group # This will allow me to make groups
from ship import Ship # This will make a ship

class Scoreboard:
    def __init__(self, game): # I initialize standard attributes

        self.game = game
        self.screen = game.screen # Standard attributes from the game class
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.text_color = (200, 200, 200) # This will store the text color
        self.font = pgf.SysFont(None, 48) # this will store font, none is for default font, and 48 specifies its size

        self.prepare_score() # I call prepare_score method
        self.prepare_high_score() # And hight score
        self.prepare_level() # And level and ships
        self.prepare_ships()

    def prepare_score(self):

        rounded_score = round(self.stats.score, -1) # This will round the score to nearest tenth
        score_string = '{:,}'.format(rounded_score) # This converts score to string
        self.score_image = self.font.render(score_string, True, self.text_color, self.settings.bg_color) # This method converts message string to image, and display it (True for anti aliasing)

        self.score_rect = self.score_image.get_rect() # This creates the rectangle and draws it on the screen
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prepare_high_score(self): # I do the same thing for hight score

        rounded_high_score = round(self.stats.high_score, -1)
        h_score_string = '{:,}'.format(rounded_high_score)
        self.h_score_image = self.font.render(h_score_string, True, self.text_color, self.settings.bg_color)

        self.h_score_rect = self.h_score_image.get_rect()
        self.h_score_rect.centerx = self.screen_rect.centerx
        self.h_score_rect.top = 20

    def prepare_level(self):

        level = self.stats.level
        level_string = 'Level: ' + format(level) # This converts score to string
        self.level_image = self.font.render(level_string, True, self.text_color, self.settings.bg_color) # This method converts message string to image, and display it (True for anti aliasing)

        self.level_rect = self.level_image.get_rect() # This creates the rectangle and draws it on the screen
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prepare_ships(self): # This creates how many ships are left

        self.ships = Group() # I make a group of ships
        for ship_num in range(self.stats.ships_left + 1): # Create a ship and set its parameters and add to ships attribute group
            ship = Ship(self.game) #
            ship.rect.x = 10 + ship.rect.width * ship_num
            ship.rect.y = -45
            self.ships.add(ship)

    def show_score(self):

        self.screen.blit(self.score_image, self.score_rect) # This draws the rectangle and value of the score on the screen
        self.screen.blit(self.h_score_image, self.h_score_rect) # Same for high score
        self.screen.blit(self.level_image, self.level_rect) # Same for level
        self.ships.draw(self.screen) # And I draw the ships (to show how many left)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.stats.write_high_score()
            self.prepare_high_score()
