# This program will store all the settings for my game in the Settings class
# It will aslo be imported into my alien_invasion program to save there space
class Settings:
    def __init__(self):

        #### Game Settings ####

        self.speed_up_multiplier = 1.1 # How quickly the game speeds up

        #### Screen Settings ####
        self.screen_width = 1200 # here I determine the width of the display screen
        self.screen_height = 800 # here I determine the height of the display screen
        self.bg_color = (0, 0, 26) # here I determine the background color of the display screen

        #### Ship Settings ####
        self.ship_limit = 3
        self.ship_limit -= 1

        #### Bullet Settings ####
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_available = 3 # This will limit the number of bullets

        #### Stars Settings ####
        self.num_of_stars = 1000
        self.score_scale = 1.5

        #### File Settins ####

        self.file_name = 'high_scores.txt'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self): # dynamic settings can be changed in game

        self.ship_speed = 5
        self.bullet_speed = 7.0

        #### Alien Settings ####
        self.fleet_drop_speed = 8 # How quickly fleet drops down when it reaches an edge
        self.fleet_direction = 1 # 1 is right, -1 is left
        self.alien_speed = 1.0
        self.diff_level = 0

        #### Scoring ####

        self.alien_point = 50

    def increase_speed(self): # This will change these settings in game
        self.ship_speed *= self.speed_up_multiplier
        self.bullet_speed *= self.speed_up_multiplier
        self.fleet_drop_speed *= self.speed_up_multiplier
        self.alien_speed *= self.speed_up_multiplier

        self.alien_point = int(self.alien_point * self.score_scale)
