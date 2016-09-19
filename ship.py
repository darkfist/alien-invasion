import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    # initialize the ship and set its starting position
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get it's rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center on the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # movement of the ship
        self.moving_right = False
        self.moving_left = False

    # update the ship's position based on the key pressed
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # move rect object from self.center
        self.rect.centerx = self.center

    # draw the ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # center the ship on the screen
    def center_ship(self):
        self.center = self.screen_rect.centerx
