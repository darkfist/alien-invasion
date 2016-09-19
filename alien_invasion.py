import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # initialize pygame, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # create an instance to store game statistics, and a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # make a ship, a group of bullets & aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop for the game
    while True:
        # respond to keypress and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            # update the ship's position based on the key pressed
            ship.update()
            # get rid of bullets that have disappeared
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            # update  aliens movement
            gf.update_aliens(ai_settings, screen, stats,
                             sb, ship, aliens, bullets)

        # update images on the screen and flip to the new screen
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)

run_game()
