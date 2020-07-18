class Settings:

    def __init__(self):

        self.screen_width = 1250
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.margin = 2
        self.box_size = 50

        # Game stats
        self.reset_stats()
        self.high_score = 0

        # Game state
        self.game_active = False

    def reset_stats(self):
        self.score = 0