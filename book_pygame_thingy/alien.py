import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        self.settings = ai_game.settings

    def update(self):
        """move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        self.screen_rect = self.screen.get_rect()
        return (self.rect.right >= self.screen_rect.right) or (self.rect.left <= 0)


class GreenAlien(Alien):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/green alien.bmp')
        self.color = "green"

class YellowAlien(Alien):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/yellow alien.bmp')
        self.color = "yellow"

class RedAlien(Alien):
    def __init__(self, ai_game):
        super().__init__(ai_game)
        self.image = pygame.image.load('images/red alien.bmp')
        self.color = "red"
        