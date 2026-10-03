import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                new_alien = Alien(self)
                new_alien.x, new_alien.y = current_x, current_y
                new_alien.rect.x, new_alien.rect.y = current_x, current_y
                self.aliens.add(new_alien)
                current_x += 2 * alien_width

            # finished a row; reset x val increment y val
            current_x = alien_width
            current_y += 2 * alien_height

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
            if len(self.bullets) < self.settings.bullets_allowed:
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
        self.aliens.draw(self.screen)
        pygame.display.flip()
    def run_game(self):
        """start the main loop for the game."""
        while True:
            self._check_events()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self.aliens.update()
            self._update_screen()
            self.ship.update()
            self.clock.tick(60)




if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()

    