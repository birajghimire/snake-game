import pygame
from pygame.locals import *
import time
import random

SNAKE_SIZE = 40

# Apple class to handle apple related functionalities
class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 80
        self.y = 80

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, (1000 - SNAKE_SIZE) // SNAKE_SIZE - 1) * SNAKE_SIZE
        self.y = random.randint(1, (500 - SNAKE_SIZE) // SNAKE_SIZE - 1) * SNAKE_SIZE

# Snake class to handle snake related functionalities
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.png").convert()
        self.x = [SNAKE_SIZE] * length
        self.y = [SNAKE_SIZE] * length
        self.direction = "down"

    def draw(self):
        # Updated the background color to black
        self.parent_screen.fill((0, 0, 0))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    # Direction control functions
    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move(self):
        # Moving the snake based on its current direction
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == "up":
            self.y[0] -= SNAKE_SIZE
        if self.direction == "down":
            self.y[0] += SNAKE_SIZE
        if self.direction == "left":
            self.x[0] -= SNAKE_SIZE
        if self.direction == "right":
            self.x[0] += SNAKE_SIZE

        # If snake goes out of bounds, end the game
        if self.x[0] < 0 or self.x[0] >= 1000 or self.y[0] < 0 or self.y[0] >= 500:
            raise Exception("Out of Bounds")

        self.draw()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

# Game class to handle game-related functionalities
class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 500))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def reset(self):
        self.snake = Snake(self.surface, 1) # Reset snake length to 5
        self.apple = Apple(self.surface)

    def is_collision(self, x1, y1, x2, y2):
        # Check for collision between two objects
        if x1 >= x2 and x1 < x2 + SNAKE_SIZE:
            if y1 >= y2 and y1 < y2 + SNAKE_SIZE:
                return True
        return False

    def play(self):
        self.snake.move()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # Check if snake ate an apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        # Check if snake collides with itself
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise Exception("Collision Occurred")

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (850, 10))

    def show_game_over(self):
        self.surface.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is over! Score: {self.snake.length} Press Enter to play again", True, (255, 255, 255))
        self.surface.blit(line1, (200, 300))
        pygame.display.flip()

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()

            except Exception as e:
                self.show_game_over()
                time.sleep(5)  # 5 seconds before restarting
                pause = True
                self.reset()

            time.sleep(.25)  # Controlling snake's speed

if __name__ == "__main__":
    game = Game()
    game.run()

    
    
    
    