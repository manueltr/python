import pygame.font

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, sn_game):
        """Initialize scorekeeping attributes."""
        self.sn_game = sn_game
        self.screen = sn_game.screen
        self.settings = sn_game.settings
        self.screen_rect = self.screen.get_rect()

        # Font settings for scorng information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()



    def prep_score(self):
        """Turn the score into a rendered image."""
        score = self.settings.score
        self.score_image = self.font.render(f"score: {score}", True,
                self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = self.settings.high_score
        self.high_score_image = self.font.render(f"Best: {high_score}",
                True, self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top



    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def check_high_score(self):
        """Check to see if there's a new highscore."""
        if self.settings.score > self.settings.high_score:
            self.settings.high_score = self.settings.score
            self.prep_high_score()