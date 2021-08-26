import pygame # I first import pygame and sprite module
from pygame.sprite import Sprite # Sprite allows to create basic game object classes

class Bullet(Sprite):
    def __init__(self, game): # Because I use sprite as father class, I can use super function to initiate bullet class
        super().__init__()
        self.screen = game.screen # I also take some attribute from the game such as screen, settings, etc
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) # Because bullet is not a photo I have to create it from a scratch using Rect() method
        self.rect.midtop = game.ship.rect.midtop# After creating the bullet I set the top of the bullet to the top of the ship
        self.y = float(self.rect.y) # self.rect.y is int, and I want bullets to have option of non-integer speeds, that's why I convert it to float using float()

    def update(self): # This method updates the position of a bullet (bullet group to be precise), and makes the bullets go up
        self.y -= self.settings.bullet_speed # I change the bullets position
        self.rect.y = self.y # and set it as their new position (in y direction)

    def draw_bullet(self): # Finally this function draws the bullets on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
