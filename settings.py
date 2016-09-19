class Settings():
    """ A class to store all Settings for Alien Invasion """

    # initialize the game's static settings
    def __init__(self):
        # screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # alien settings
        self.fleet_drop_speed = 8

        # how quickly the game speeds up
        self.speedup_scale = 1.1

        # how quickly the alien points value increase
        self.score_scale = 1.2

        # initializing dynamic settings
        self.initialize_dynamic_settings()

    # initialize settings that change throughout the game
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    # settings to increase speed and scoring points
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
