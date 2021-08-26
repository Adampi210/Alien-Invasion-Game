# This class will store all statistics of the game
# Most will be in reset stats so that player can start new game

class GameStats:
    def __init__(self, game): # In init I define settings, and call reset_stats
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False # This variable tells if the user is still playing, if the user loses it changes is False
        # It starts as False, player will inititate new game
        self.high_score = 0
        self.get_high_score()

        self.level = 1


    def reset_stats(self): # Here I will set the stats to default
        self.ships_left = self.settings.ship_limit # Number of ship lives
        self.score = 0

    def get_high_score(self):
        file_name = self.settings.file_name
        file = open(file_name, 'r', encoding = 'UTF8')
        self.high_score = int(file.read())
        file.close()

    def write_high_score(self):
        file_name = self.settings.file_name
        file = open(file_name, 'w', encoding = 'UTF8')
        file.write(str(self.high_score))
        file.close()
