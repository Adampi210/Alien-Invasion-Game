# This class will store button. Thanks to it I will be able to show messages on screen
import pygame as pg # I import pygame module
import pygame.font as pgf # And I import font module to print messages on screen
class Button: # Then I create a class, and inititate it with game, and message that should be printed
    def __init__(self, game, message, position, width = 200, height = 50):
        self.screen = game.screen # I get standard variables
        self.screen_rect = self.screen.get_rect()

        # Here I set the properties of the button
        self.width = width
        self.height = height
        self.button_color = (0, 255, 100)
        self.text_color = (255, 255, 255)
        self.font = pgf.SysFont(None, 48) # none is for default font, and 48 specifies its size

        # Here I set the position of the button
        self.rect = pg.Rect(0, 0, self.width, self.height)
        if position == 0:
            self.rect.center = self.screen_rect.center
        elif position == 1:
            self.rect.bottomleft = self.screen_rect.bottomleft
            self.rect.y -= self.height
            self.button_color = game.settings.bg_color
        else:
            self.rect.bottomleft = self.screen_rect.bottomleft
            self.rect.x += self.width * (position - 2)
            self.button_color = game.settings.bg_color
        self._show_msg(message)

    def _show_msg(self, message):

        # This method converts message string to image, and display it
        # True is for antialiasing on or off (here it is on)
        # The rest of arguments are easy to understand
        self.message_img = self.font.render(message, True, self.text_color, self.button_color)
        self.message_img_rect = self.message_img.get_rect()
        self.message_img_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) # This will draw the button, and the message
        self.screen.blit(self.message_img, self.message_img_rect)
