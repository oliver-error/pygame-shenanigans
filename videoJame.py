import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
class AlienInvasion:
    """overall class to manage game assets and behavior"""
    def __init__(self):
        """initlize the game and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_color = (0, 0, 255)
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")
        self.bullets = pygame.sprite.Group()
    def _check_events(self):
        # watch for keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # register display changes
        self.ship.blitme()
        pygame.display.flip()
    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            self.bullets.update()
            self._update_screen()
            self.ship.update()
            self.clock.tick(60)




if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

    