import sys
import pygame

from random import random
from settings import Settings
from button import Button
from scoreboard import Scoreboard

class SnakeGame:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                 self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        self.button = Button(self, "Play")

        self.grid = []
        self._create_board()

        # Initialize score board
        self.sb = Scoreboard(self)
        
        # Create movement flags
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        
        # set apple and snake cooridinates
        self._set_starting_pos()

        # Update board
        self._update_board()
        self.button.draw_button()

        # To not allow player to go left at the start
        self.first_move = True
    
    def run_game(self):
        """ Main game loop. """
        while True:

            pygame.time.wait(115)
            self._check_events()

            if self.settings.game_active:
                self._move_snake()
                self._update_board()

            self._check_game_status()
            self.sb.show_score()
            pygame.display.flip()

    def _check_game_status(self):
        """Check whether the player lost or not."""
        head = self.snake[0]
        # If snake head is outside of grid or in itself, end game.
        if (head in self.snake[1:] or head[0] < 0 or
            head[0] > self.number_of_rows - 1 or head[1] < 0 or
            head[1] > self.number_of_columns - 1):

            pygame.mouse.set_visible(True)
            self.button.draw_button()
            self._set_starting_pos()
            self.settings.game_active = False
            self._reset_movement()
            self.settings.high_score = self.settings.score
            self.settings.reset_stats()

    def _set_starting_pos(self):
        """Set snake and food starting position."""
        self.snake = [[1, 3], [1, 2], [1, 1]]
        self.apple_cord = [1, 10]

    def _reset_movement(self):
        """Resets movement flags."""
         # Create movement flags
        self.right = False
        self.left = False
        self.up = False
        self.down = False

    def _check_events(self):
        """Function to check player input."""

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and self.settings.game_active:
            if event.key == pygame.K_RIGHT and not self.left:
                self._reset_movement()
                self.right = True
            elif (event.key == pygame.K_LEFT and not self.right and 
                    not self.first_move):
                self._reset_movement()
                self.left = True
            elif event.key == pygame.K_UP and not self.down:
                self._reset_movement()
                self.up = True
            elif event.key == pygame.K_DOWN and not self.up:
                self._reset_movement()
                self.down = True
            self.first_move = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_clicked = self.button.rect.collidepoint(mouse_pos)
            if button_clicked and not self.settings.game_active:
                self._start_game()

    def _start_game(self):
        pygame.mouse.set_visible(False)
        self.sb.prep_score()
        self.settings.game_active = True
        self.settings.reset_stats()
        self.screen.fill(self.settings.bg_color)
        self.first_move = True

    def _move_snake(self):
        "Update snake location depending on movement flags."
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

        remaining_space = screen_height - box_size - 100
        self.number_of_rows = remaining_space // (box_size
            + self.settings.margin)

        for row in range(self.number_of_rows):
            self.grid.append([])
            for column in range(self.number_of_columns):
                self.grid[row].append(0)

    def _create_apple(self):
        """Create apple grid coordinates. """

        while True:
            apple_row = int(self.number_of_rows * random())
            apple_column = int(self.number_of_columns * random())
            if [apple_row, apple_column] not in self.snake:
                break

        self.apple_cord = [apple_row, apple_column]

    def _update_board(self):
        """Draw the grid, snake, and food onto screen."""
        self.screen.fill(self.settings.bg_color)

        # Check if snake ate food
        if self.snake[0] == self.apple_cord:
            self.snake.append(self.snake[-1:])

            # Update score
            self.settings.score += 1
            self.sb.prep_score()
            self.sb.check_high_score()

            # Create new apple
            self._create_apple()

        box_size = self.settings.box_size
        color = (83, 83, 83)
        for row in range(self.number_of_rows):
            for column in range(self.number_of_columns):
                coordinate = [row, column]

                # draw snake, grid and food
                if coordinate in self.snake:
                    if coordinate == self.snake[0]:
                        color = (0, 0, 255)
                    else:
                        color = (255, 255, 255)
                elif coordinate == self.apple_cord:
                    color = (255, 0, 0)
                else:
                    color = (83, 83, 83)
                
                square = pygame.rect.Rect(int(box_size + (box_size + 2)*column),
                    int(100 + (box_size + 2)*row), box_size, box_size)
                pygame.draw.rect(self.screen, color, square, 0)
     
if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()