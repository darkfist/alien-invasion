import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a alien in the fleet """

    # initialize the alien and set its starting position
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact position in decimal value
        self.x = float(self.rect.x)

    # draw the alien at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # return True if alien is at edge of screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    # move the alien right or left
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
