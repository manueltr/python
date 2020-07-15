import sys
import pygame

from settings import Settings

class SnakeGame:

    def __init__(self):

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                 self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        self._create_board()
    
    def run_game(self):
        while True:
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _create_board(self):
        self.screen.fill(self.settings.bg_color)
        box_size = self.settings.box_size

        screen_width, screen_height = (self.settings.screen_width,
                self.settings.screen_height)
        remaining_space = screen_width - 2 * box_size
        number_of_columns = remaining_space // (box_size
            + self.settings.margin)

        remaining_space = screen_height - 2 * box_size
        number_of_rows = remaining_space // (box_size
            + self.settings.margin)

        for column in range(number_of_columns):
            for row in range(number_of_rows):
                square = pygame.rect.Rect(int(box_size + (box_size + 2)*column),
                    int(box_size + (box_size + 2)*row), box_size, box_size)
                pygame.draw.rect(self.screen, (83,83,83), square, 0)

                
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()