# This is the first program in the alien invasion game project
# This program will setup the game window and draw the elements like ship, aliens, etc
# Before running this program check if the pygame module is installed
# If not use python -m pip install --user pygame in command mode to install the module into python
# If the module is installed the program can begin
# First thing is to import the module
import sys # This module provides access to variables used by the interpreter (the game screen)
from time import sleep # I import sleep from time so that I can freeze the screen
import pygame as pg # This module contains everything we need to make 5a game
from settings import Settings # This module imports settings
from ship import Ship # This module imports the ship class
from bullet import Bullet # This module imports Bullet class
from alien import Alien # This module imports Alien class
from stars import Star # I import Star from stars
from game_stats import GameStats # I import GameStats
from button import Button # I import Button
from scoreboard import Scoreboard # I import Scoreboard

class AlienInvasion:
    # Class to manage the game
    def __init__(self):
        pg.init()
        # here I initiate the pygame module, and setup the display which will be our screen
        # I also set the caption of the display to be Alien Invasion Game
        self.settings = Settings() # I use the settings class to store all game settings
        #self.screen = pg.display.set_mode((self.settings.screen_width, self.settings.screen_height)) # I can determine the size of the screen
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("Alien Invasion Game") # Here I set the name for the display
        self.ship = Ship(self) # Here I create ship attribute using ship class written in ship.py program
        self.bullets = pg.sprite.Group() # because there will be many bullets I create a group
        self.aliens = pg.sprite.Group() # I do the same for aliens as there will be many of them
        # To do that I use sprite - module with basic game classes
        # Group() can hold multiple game objects
        # Thanks to using group we can update all the present elements (bullets) at once
        self._create_fleet() # This function will create a fleet of aliens on the screen
        self.stars = pg.sprite.Group() # This will hold all the stars as a group
        self._create_stars() # And this will create the stars determining their positions
        self.stats = GameStats(self) # This initiates stats module
        self.play_button = Button(self, 'Play', 0) # This inititates the button
        self.diff_button = Button(self, 'Select Difficulty', 1, 450)
        self.diff_1_button = Button(self, 'Easy', 2, 150)
        self.diff_2_button = Button(self, 'Medium', 3, 150)
        self.diff_3_button = Button(self, 'Hard', 4, 150)
        self.sb = Scoreboard(self) # I create a scoreboard

    def run_game(self): # This method runs the game, making sure that the game runs unless the user wants to exit
        while 1: # this loop runs all the time and contains the event loop and a code that updates the screen
            self._check_events() # This help function checks for events (mostly key presses) and runs instructions connected to them
            if self.stats.game_active: # The following commands only run when the player has lives left
                self.ship.update() # This function updates the position of the ship
                self._update_bullets() # This helper method updates all the bullets positions, and delets the old ones
                self._update_aliens()

            self._update_screen() # This help function updates the screen

    def _check_events(self): # this is a helper method used to make run_game method shorter (helper methods start with _)
    # this method checks for the events
        for event in pg.event.get(): # the event loop looks for events. An event is an action that the user performs like clicking key or pressing mouse. for loop checks for events and performs tasks accordingly
        # Also the pg.event.get() function returns a list of all events that occured since the last time that function was called (so since last while loop iteration)
        # In other words the while goes continuously, and has a for loop that checks for events and goes through every event
            if event.type == pg.QUIT: # if the for loop detects that a player closed the game's window close button
                sys.exit() # it exits the game (by calling sys.exit())
            elif event.type == pg.KEYDOWN: # if the function detects that a key was pressed it checks which key was that
                self._check_keydown_events(event)

            elif event.type == pg.KEYUP: # if the function detects that given keys are up
                self._check_keyup_events(event)

            elif event.type == pg.MOUSEBUTTONDOWN: # If I press the button
                mouse_pos = pg.mouse.get_pos() # Then I read the position of mouse
                self._check_play_button(mouse_pos) # And I check if the position was over play button while clicking
                self._check_diff_button(mouse_pos) # And checks if the Difficulty was chosen

    def _check_keydown_events(self, event):
        if event.key == pg.K_d:
            self.ship.moving_right = True # and sets the attribute of the ship movement to true, which makes the ship move
        elif event.key == pg.K_a:
            self.ship.moving_left = True
        elif event.key == pg.K_w:
            self.ship.moving_up = True
        elif event.key == pg.K_s:
            self.ship.moving_down = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE: # If I press space, I fire bullets
            self._fire_bullets()
        elif event.key == pg.K_p:
            self._start_game()

    def _check_keyup_events(self, event):
        if event.key == pg.K_d:
            self.ship.moving_right = False # it sets the ship movement attributes to false
        elif event.key == pg.K_a:
            self.ship.moving_left = False
        elif event.key == pg.K_w:
            self.ship.moving_up = False
        elif event.key == pg.K_s:
            self.ship.moving_down = False

    def _fire_bullets(self): # This helper method fires bullets
        if len(self.bullets) < self.settings.bullets_available: # This limits the max number of bullets that can be on screen, which will limit the fire rate of the ship
            new_bullet = Bullet(self) # Every time it is called it creates a new bullet
            self.bullets.add(new_bullet) # And adds the bullet to the group of alreay present bullets

    def _update_screen(self): # This is another helper method that I will use to uptade the screen every
    # I call this method every iteration of a loop
        self.screen.fill(self.settings.bg_color) # Every loop I set the bgcolor to be determined, this command fills the screen with the determined color
        for star in self.stars.sprites(): # Then I draw the stars on the screen
            star.draw_star() # I also draw the stars on the screen (every star in self.stars group)

        self.ship.blitme() # and here I draw the ship on the screen using blitme method defined in Ship class

        for bullet in self.bullets.sprites(): # Finally, in update screen method, for every bullet
            bullet.draw_bullet() # I draw it on the screen

        self.aliens.draw(self.screen) # I also draw the aliens on the screen

        if not self.stats.game_active: # This draws play button if the game is not active
            self.play_button.draw_button()
            self.diff_button.draw_button()
            self.diff_1_button.draw_button()
            self.diff_2_button.draw_button()
            self.diff_3_button.draw_button()

        self.sb.show_score() # I draw the score on the screen

        pg.display.flip() # this updates the screen after user does something, the screen is updated every iteration of a loop (as this method runs in while 1 loop)

    def _update_bullets(self):
        self.bullets.update() # Every time game runs, I update the position of the bullets present

        for bullet in self.bullets.copy(): # this loop is similar to others, but insetead of the self.bullets list, it uses its copy
        # That is because I shouldnt change the limits of the loop inside a loop, as it can lead to mistakes
        # And by deleting the bullets we change I list, so I change the limit of the loop
        # That is why I use a copy of bullet list - one that will not change
            if bullet.rect.bottom <=0: # then in that loop, if I detect that the bullet is off screen
                self.bullets.remove(bullet) # I delete it

        self._check_bullets_alien_collisions() # Check for collisions if bullets collided with aliens

    def _check_bullets_alien_collisions(self):
        collisionsAliens = pg.sprite.groupcollide(self.bullets, self.aliens, True, True) # This detects collisions and kills aliens when they collide with bullet (removes bullets and aliens)
        if not self.aliens: # This checks if the fleet of aliens was destroyed, if it has then
            self.bullets.empty() # Delete remaining bullets (so that old bullets dont shoot new aliens)
            self._create_fleet() # create a new fleet
            self.settings.increase_speed() # This will incease all speeds

            self.stats.level += 1 # And increase the level of the game
            self.sb.prepare_level()

        if collisionsAliens: # If a bullet collides with alien, it adds score for every alien hit
            for aliens in collisionsAliens.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prepare_score()
            self.sb.check_high_score()

    def _create_fleet(self): # This method will create aliens on the screen
        alien = Alien(self) # First I create an alien object (this alien wont be in a flee, I just use it to get data)
        alien_width, alien_height = alien.rect.size # and I get its width and height, as I will use it to determine number of aliens on screen

        available_space_x = self.settings.screen_width - (2 * alien_width) # I set the available space to be the width of the screen - the width of the first alien that I created - first empty space (the same as width of alien so *2)
        numof_aliens_x = available_space_x // (2 * alien_width) # then I calculate how many I should add by dividing available space by sum od widths of alien and empty space (2 * alien width)

        ship_height = self.ship.rect.height # Basically the same but as width for y
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        numof_rows = available_space_y // (2 * alien_height)

        for row in range(numof_rows): # For every row
            for alien_num in range(numof_aliens_x): # I then for the calculated number of aliens create the fleet using _create_alien helper method
                self._create_alien(alien_num, row)

    def _create_alien(self, alien_num, row):
        alien = Alien(self) # I create a new alien
        alien_width, alien_height = alien.rect.size # I have to get width and height as it is not in this function
        alien.x = alien_width + 2 * alien_width * alien_num # and draw it on a appropriate place, starting with alien 0 on alien_width, and then incrementing by 2 alien_width
        alien.rect.x = alien.x # I set the int value to the alien.x value
        alien.rect.y = alien_height + 2 * alien_height * row
        self.aliens.add(alien) # and I add it to the group of our aliens

    def _check_fleet_edges(self): # This method will check if the fleet has reached the edge
        for alien in self.aliens.sprites(): # For every alien in the group it checks if it reached the edge
            if alien.check_edges():
                self._change_fleet_direction() # And if they have it changes the direction of the fleet and breaks the loop so that it can start checking again
                break # It is important that it goes through all aliens, ans we want it to ignore aliens that have been shot down

    def _change_fleet_direction(self): # This changes the direction of the fleet once it reaches the edge
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed # For every alien, it changes its position down by given speed
        self.settings.fleet_direction *= -1 # And change the direction of the fleet in x axis

    def _update_aliens(self): # This updates the aliens positions
        self._check_fleet_edges() # It first checks if the fleet has reached the edges
        self.aliens.update() # And then it updates the fleet's position

        if pg.sprite.spritecollideany(self.ship, self.aliens): # This function takes two arguments: sprite and a group. It then looks for any members of the group that collided with the sprite
        # And stops looping through group if it detects collision (it returns the number of alien it collided with, which is > 0 so if will work)
            self._ship_hit()

        self._check_aliens_bottom() # This checks if any alien reached the bottom of screen

    def _check_aliens_bottom(self): # This method checks if any of te aliens have reached the bottom of the screen
        screen_rectangle = self.screen.get_rect() # I create variable storing the screen rectangle
        for alien in self.aliens.sprites(): # And the for every alien
            if alien.rect.bottom >= screen_rectangle.bottom: # I check if it reached the bottom of the screen
                self._ship_hit() # If it has I treat it as if the ship was hit
                break # and break the loop, and start again

    def _ship_hit(self): # This method tells what to do if the ship was hit
        if self.stats.ships_left > 0: # If the player has any lives left
            self.stats.ships_left -= 1 # First it decreases the number of ship lives
            self.sb.prepare_ships()

            self.aliens.empty() # This empties the screen of aliens and bullets
            self.bullets.empty()

            self._create_fleet() # And this creates a new fleet and centers the ship
            self.ship.center_ship()

            sleep(0.5) # And this freezes the screen for half a second
        else:
            self.stats.game_active = False # If not, you lost
            pg.mouse.set_visible(True)

    def _check_play_button(self, mouse_pos): # This method checks if the position is over the button
        button_clicked = self.play_button.rect.collidepoint(mouse_pos) # this checks the button is in a collide point with mouse

        if button_clicked and not self.stats.game_active: # It checks if the button was clicked when the game was not active
            self._start_game() # This starts the game

    def _check_diff_button(self, mouse_pos):
        diff1 =  self.diff_1_button.rect.collidepoint(mouse_pos)
        diff2 =  self.diff_2_button.rect.collidepoint(mouse_pos)
        diff3 =  self.diff_3_button.rect.collidepoint(mouse_pos)

        if diff1:
            self.settings.speed_up_multiplier = 1.1
        elif diff2:
            self.settings.speed_up_multiplier = 1.6
        elif diff3:
            self.settings.speed_up_multiplier = 2.1


    def _create_stars(self): # This method will randomly create given number of stars on the screen
        for star in range(self.settings.num_of_stars):
            new_star = Star(self) # I create a new star with random coordinates
            self.stars.add(new_star) # and add it to the group

    def _start_game(self):
        self.settings.initialize_dynamic_settings()

        pg.mouse.set_visible(False) # This makes the mouse invisible

        self.stats.reset_stats() # It resets the statistics
        self.stats.game_active = True # If it is, the game starts

        self.aliens.empty() # This empties the aliens and bullets
        self.bullets.empty()

        self._create_fleet() # and creates new fleet, and centers the button
        self.ship.center_ship()

        self.sb.prepare_score() # This resets the score
        self.sb.prepare_level() # And this resets the level
        self.sb.prepare_ships() # And this finally draws the ship

def main():
    alien_inv_game = AlienInvasion()
    alien_inv_game.run_game()

main()
