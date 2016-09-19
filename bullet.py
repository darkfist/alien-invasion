import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    # create a bullet object at the ship's current position
    def __init__(self, ai_settings, screen, ship, bullet):
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        # set the color of the bullet
        self.color = ai_settings.bullet_color
        # set the speed of the bullet
        self.speed_factor = ai_settings.bullet_speed_factor

    # move the bullet up the screen
    def update(self):
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    # draw the bullet to the screen
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
