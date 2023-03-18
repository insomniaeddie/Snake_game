import pygame
import sys
import random


class SnakeGame:
    def __init__(self):
        # Set screen size
        self.screen_width = 500
        self.screen_length = 550
        self.grid_size = 10

        # Initialize the pygame library
        pygame.init()

        # Create a title for the game
        pygame.display.set_caption('Snake game by YC')
        # Set up the screen display
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_length))

        # Set the initial position and length of the snake
        self.snake_positionX = 20
        self.snake_positionY = 100
        self.snake_size = self.grid_size
        self.snake_length = 1
        self.snake_blocks = []

        self.x1_change = 0
        self.y1_change = 0

        # Set the initial position of the fruit
        self.fruit_positionX = random.randrange(
            1, self.screen_width // self.grid_size) * self.grid_size
        self.fruit_positionY = random.randrange(
            1, self.screen_length // self.grid_size) * self.grid_size
        self.fruit_size = self.grid_size
        self.fruit_spawn = True

        # Set initial score
        self.score = 0

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.y1_change != self.grid_size:
                    self.x1_change = 0
                    self.y1_change = -self.grid_size
                elif event.key == pygame.K_DOWN and self.y1_change != -self.grid_size:
                    self.x1_change = 0
                    self.y1_change = self.grid_size
                elif event.key == pygame.K_LEFT and self.x1_change != self.grid_size:
                    self.x1_change = -self.grid_size
                    self.y1_change = 0
                elif event.key == pygame.K_RIGHT and self.x1_change != -self.grid_size:
                    self.x1_change = self.grid_size
                    self.y1_change = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_snake(self):
        self.snake_positionX += self.x1_change
        self.snake_positionY += self.y1_change

        # Check if the snake has hit the border
        if (self.snake_positionX < 0 or self.snake_positionX >= self.screen_width or
                self.snake_positionY < 0 or self.snake_positionY >= self.screen_length):
            self.game_over = True

        snake_head = [self.snake_positionX, self.snake_positionY]
        self.snake_blocks.append(snake_head)

        if len(self.snake_blocks) > self.snake_length:
            del self.snake_blocks[0]

        for x in self.snake_blocks[:-1]:
            if x == snake_head:
                self.game_over = True

        if self.snake_positionX == self.fruit_positionX and self.snake_positionY == self.fruit_positionY:
            self.fruit_positionX = random.randrange(
                1, (self.screen_width // 10)) * 10
            self.fruit_positionY = random.randrange(
                1, (self.screen_length // 10)) * 10
            self.snake_length += 1

            self.fruit_spawn = True

    def draw_snake(self):
        self.screen.fill((0, 0, 0))
        for block in self.snake_blocks:
            pygame.draw.rect(self.screen, pygame.Color('green'), pygame.Rect(
                block[0], block[1], self.snake_size, self.snake_size))
        pygame.draw.rect(self.screen, pygame.Color('red'), pygame.Rect(
            self.fruit_positionX, self.fruit_positionY, self.fruit_size, self.fruit_size))
        pygame.display.update()
        self.clock.tick(15)

    def show_start_prompt(self):
        font = pygame.font.Font(None, 36)

        start_button = pygame.draw.rect(
            self.screen, (255, 0, 0), (self.screen_width // 2 - 100, self.screen_length // 2, 200, 50))
        start_text = font.render("Start New Game", True, (255, 255, 255))
        start_text_rect = start_text.get_rect(center=start_button.center)
        self.screen.blit(start_text, start_text_rect)

        pygame.display.update()

        while True:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    if start_button.collidepoint(x, y):
                        return

    def game_over_prompt(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.screen_width // 2, self.screen_length // 2 - 100))
        self.screen.blit(text, text_rect)

        try_again_button = pygame.draw.rect(
            self.screen, (255, 0, 0), (self.screen_width // 2 - 100, self.screen_length // 2, 200, 50))
        try_again_text = font.render("Start a new game", True, (255, 255, 255))
        try_again_text_rect = try_again_text.get_rect(
            center=try_again_button.center)
        self.screen.blit(try_again_text, try_again_text_rect)

        exit_button = pygame.draw.rect(self.screen, (255, 0, 0), (
            self.screen_width // 2 - 100, self.screen_length // 2 + 100, 200, 50))
        exit_text = font.render("Exit", True, (255, 255, 255))
        exit_text_rect = exit_text.get_rect(center=exit_button.center)
        self.screen.blit(exit_text, exit_text_rect)

        pygame.display.update()

        while True:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    if try_again_button.collidepoint(x, y):
                        return True

                    if exit_button.collidepoint(x, y):
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    game = SnakeGame()  # Create an instance of SnakeGame class
    while True:
        game.show_start_prompt()

        while not game.game_over:  # Run the game until game_over is True
            game.handle_events()   # Handle user events
            game.update_snake()    # Update the snake position
            game.draw_snake()      # Draw the snake and fruit on the screen

        retry = game.game_over_prompt()

        if not retry:
            break
        game = SnakeGame()
