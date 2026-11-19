from pathlib import Path
import json

class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.high_score = json.loads(Path("book_pygame_thingy/high_score.json").read_text())
        self.level = 1
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
