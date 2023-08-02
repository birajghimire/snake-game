import pygame
from pygame.locals import *
import time

SNAKE_SIZE = 40

class Apple:
    def __init__(self,parent_screen):
        #initial location
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 80
        self.y = 80
        
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.flip()
    
class Snake:
    def __init__(self, parent_screen,length):
        self.parent_screen = parent_screen
        self.length = length
        self.block = pygame.image.load("resources/block.png").convert()
        self.x = [SNAKE_SIZE]*length
        self.y = [SNAKE_SIZE]*length
        self.direction = "up" # Initial direction
        
        
    def draw(self):
        self.parent_screen.fill((110,110,5))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.flip()
        

    def move(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
            
        if self.direction == "up":
            self.y[0] -= SNAKE_SIZE
        if self.direction == "down":
            self.y[0] += SNAKE_SIZE
        if self.direction == "left":
            self.x[0] -= SNAKE_SIZE
        if self.direction == "right":
            self.x[0] += SNAKE_SIZE
        
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000,500))
        self.snake = Snake(self.surface,5)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE or event.key == K_q:
                        running = False
                    elif event.key == K_UP:
                        self.snake.direction = "up"
                    elif event.key == K_DOWN:
                        self.snake.direction = "down"
                    elif event.key == K_LEFT:
                        self.snake.direction = "left"
                    elif event.key == K_RIGHT:
                        self.snake.direction = "right"
                elif event.type == QUIT:
                    running = False
            self.snake.move()
            self.apple.draw()
            time.sleep(0.2)  
        

if __name__ == "__main__":
    game = Game()
    game.run()

    
                
    
    
    
    
    