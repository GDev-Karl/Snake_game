import pygame
from pygame.math import Vector2
import random
pygame.init()

size = 30
number = 20
clock = pygame.time.Clock()
run = True
screen = pygame.display.set_mode((number * size, number * size))

class Snake:
    def __init__(self):

        """ Serpent"""
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw(self):

        """dessin du serpent"""
        for block in self.body:
            x = block.x * size
            y = block.y * size
            snake_rect = pygame.Rect(x, y, size, size)
            pygame.draw.rect(screen, (123, 123, 156), snake_rect)

    def move(self): # A revoir et a refaire 

        """ deplacement du serpent """
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

class Apple:  

    def __init__(self):

        """ dessin de la pomme à l'ecran """
        self.x = 1
        self.y = 1
        self.pos = Vector2(self.x, self.y)

    def draw(self):

        """ Methode permettant de dessiner la pomme """
        apple_rect = pygame.Rect(self.pos.x * size, self.pos.y * size , size, size)
        pygame.draw.rect(screen, (126,166, 114), apple_rect)
        
class Main:
    def __init__(self):

        """" Deroulement du jeu """
        self.snake = Snake()
        self.apple = Apple()

    def update(self):

        """ met a jour le deplacement du serpent """
        self.snake.move()

    def draw_images(self):

        """ dessine les elements à l'ecran"""
        self.apple.draw()
        self.snake.draw()

    def checkk_collision(self):
 
        """ Verification des collisions """
        if self.apple.pos == self.snake.body[0]:
            pass

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 150)
game = Main()
snake = game.snake
apple = game.apple

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
        if event.type == UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
    screen.fill((175, 215, 70))
    game.draw_images()
    pygame.display.update()
    clock.tick(60)

pygame.quit()


