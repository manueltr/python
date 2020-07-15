import sys
import pygame

from random import random
from settings import Settings

class SnakeGame:

    def __init__(self):

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                 self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        self.grid = []
        self._create_board()
        self.snake = [[1, 3], [1, 2], [1, 1]]
        
        # Create movement flags
        self.right = True
        self.left = False
        self.up = False
        self.down = False
        

    def run_game(self):
        """ Main game loop. """
        while True:
            pygame.time.wait(120)
            self._check_events()
            self._move_snake()
            self._update_board()
            pygame.display.flip()

    def _reset_movement(self):
        """Resets movement flags."""
         # Create movement flags
        self.right = False
        self.left = False
        self.up = False
        self.down = False


    def _check_events(self):
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not self.left:
                self._reset_movement()
                self.right = True
            elif event.key == pygame.K_LEFT and not self.right:
                self._reset_movement()
                self.left = True
            elif event.key == pygame.K_UP and not self.down:
                self._reset_movement()
                self.up = True
            elif event.key == pygame.K_DOWN and not self.up:
                self._reset_movement()
                self.down = True

    def _move_snake(self):
        if self.right:
            self.snake.insert(0, [self.snake[0][0], self.snake[0][1] + 1])
            self.snake.pop()
        elif self.left:
            self.snake.insert(0, [self.snake[0][0], self.snake[0][1] - 1])
            self.snake.pop()
        elif self.up:
            self.snake.insert(0, [self.snake[0][0] - 1, self.snake[0][1]])
            self.snake.pop()
        elif self.down:
            self.snake.insert(0, [self.snake[0][0] + 1, self.snake[0][1]])
            self.snake.pop()

    def _create_board(self):
        """Create board grid."""
        self.screen.fill(self.settings.bg_color)
        box_size = self.settings.box_size

        screen_width, screen_height = (self.settings.screen_width,
                self.settings.screen_height)
        remaining_space = screen_width - 2 * box_size
        self.number_of_columns = remaining_space // (box_size
            + self.settings.margin)

        remaining_space = screen_height - 2 * box_size
        self.number_of_rows = remaining_space // (box_size
            + self.settings.margin)

        for row in range(self.number_of_rows):
            self.grid.append([])
            for column in range(self.number_of_columns):
                self.grid[row].append(0)

    def _update_board(self):
        """Draw grid onto board."""
        box_size = self.settings.box_size
        color = (83, 83, 83)
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                coordinate = [row, column]
                if coordinate in self.snake:
                    color = (255, 255, 255)
                else:
                    color = (83, 83, 83)
                square = pygame.rect.Rect(int(box_size + (box_size + 2)*column),
                    int(box_size + (box_size + 2)*row), box_size, box_size)
                pygame.draw.rect(self.screen, color, square, 0)
                

                
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()