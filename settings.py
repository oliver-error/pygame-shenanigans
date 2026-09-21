class Settings:
    """a class to store all settings for Alien Invasion"""
    def __init__(self):
        """initalize the game's settings"""
        # Screen settings 
        self.screen_height = 800
        self.screen_width = 1200
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 4

        # bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

