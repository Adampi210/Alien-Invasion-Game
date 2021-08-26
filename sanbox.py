import sys # This module provides access to variables used by the interpreter (the game screen)
import pygame as pg # This module contains everything we need to make a game
from pygame.sprite import Sprite

class Ai:
    def __init__(self):

        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.new_bullet = Bullet(self)
        self.new_bullet.draw_bullet()

    def run_game(self): # This method runs the game, making sure that the game runs unless the user wants to exit
        while 1:
            self._check_events()
            self.screen.fill('#000000')
            self.new_bullet.update()
            self.new_bullet.draw_bullet()
            self.bullets = pg.sprite.Group()

            pg.display.flip()


    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    sys.exit()

##### naprawic bullet, bo nie dziala (nie wywala ale nie pokazuje)
class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.color = (100, 100, 100)

        self.rect = pg.Rect(0, 0, 400, 400)
        self.rect.midtop = self.screen_rect.midbottom

        self.rect.y = 0

    def update(self):
        print(self.rect.y)
        self.rect.y += 1

    def draw_bullet(self):
        pg.draw.rect(self.screen,self.color,(1000 ,self.rect.y,100,50))
        # 1 to x value
        # 2 to y value
        # 3 to width
        # 4 to height
        #pg.draw.rect(self.screen, self.color, self.rect)


game = Ai()
game.run_game()
