import pygame
import sys
import random


class SnakeGame:
    def __init__(self):
        # Set screen size
        self.screen_width = 600
        self.screen_length = 720

        # initialize the pygame library
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
        self.snake_size = 5
        self.snake_length = 1
        self.snake_blocks = []

        self.x1_change = 0
        self.y1_change = 0

        # Set the initial position of the fruit
        self.fruit_positionX = random.randrange(
            1, (self.screen_width//10)) * 10
        self.fruit_positionY = random.randrange(
            1, (self.screen_length//10)) * 10
        self.fruit_spawn = True

        # Set initial score
        self.score = 0

        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            # To get user input from keyboard to move the snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.x1_change = 0
                    self.y1_change = -5
                if event.key == pygame.K_DOWN:
                    self.x1_change = 0
                    self.y1_change = 5
                if event.key == pygame.K_LEFT:
                    self.x1_change = -5
                    self.y1_change = 0
                if event.key == pygame.K_RIGHT:
                    self.x1_change = 5
                    self.y1_change = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_snake(self):
        # Set the position of the snake head
        snake_head = []
        snake_head.append(self.snake_positionX)
        snake_head.append(self.snake_positionY)
        self.snake_blocks.append(snake_head)

        # Check if any block except last one is touching the snake head
        for x in self.snake_blocks[:-1]:
            if x == snake_head:
                self.game_over = True

        if self.snake_positionX == self.fruit_positionX and self.snake_positionY == self.fruit_positionY:
            self.fruit_positionX = round(random.uniform(
                0, self.screen_width - self.snake_size) / 10.0) * 10.0
            self.fruit_positionY = round(random.randrange(
                0, self.screen_length - self.snake_size) / 10.0) * 10.0
            self.snake_length += 1

            self.fruit_spawn = True

        # Update the position of each block of the snake
        if len(self.snake_blocks) > self.snake_length:
            del self.snake_blocks[0]

        # Update the position of the snake head
        self.snake_positionX += self.x1_change
        self.snake_positionY += self.y1_change

    # Draw the snake
        for block in self.snake_blocks:
            pygame.draw.rect(self.screen, pygame.Color('blue'), pygame.Rect(
                block[0], block[1], self.snake_size, self.snake_size))

    # Draw the fruit
        if self.fruit_spawn:
            pygame.draw.rect(self.screen, pygame.Color('red'), pygame.Rect(
                self.fruit_positionX, self.fruit_positionY, self.snake_size, self.snake_size))
            self.fruit_spawn = False

    # Update the display and set the clock
        pygame.display.update()
        self.clock.tick(60)
