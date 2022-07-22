from email.quoprimime import body_check
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
        self.direction = Vector2(1, 0) #indique la direction de deplacement du serpent
        self.add = False

    def draw(self):

        """dessin du serpent"""
        for block in self.body:
            x = block.x * size
            y = block.y * size
            snake_rect = pygame.Rect(x, y , size, size)
            pygame.draw.rect(screen, (123, 123, 156), snake_rect)

    def move(self):

        """ deplacement du serpent """
        if self.add:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[:-1] #on recupère tout les éléments de la liste sauf le dernier
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):

        """ ajout d'un nouveau block """
        self.add = True

class Apple:  

    def __init__(self):

        """ dessin de la pomme à l'ecran """
        self.ramdomize()

    def draw(self):

        """ Methode permettant de dessiner la pomme """
        apple_rect = pygame.Rect(self.pos.x * size, self.pos.y * size , size, size)
        pygame.draw.rect(screen, (126,166, 114), apple_rect)

    def ramdomize(self):
        self.x = random.randint(0, number - 1)
        self.y = random.randint(0, number - 1)
        self.pos = Vector2(self.x, self.y)
        
class Main:

    def __init__(self):

        """" Deroulement du jeu """
        self.snake = Snake()
        self.apple = Apple()

    def update(self):

        """ met a jour le deplacement du serpent """
        self.snake.move()
        self.check_hit()

    def draw_images(self):

        """ dessine les elements à l'ecran"""
        self.apple.draw()
        self.snake.draw()

    def check_collision(self):
 
        """ Verification des collisions """
        if self.apple.pos == self.snake.body[0]:
            self.apple.ramdomize()
            self.snake.add_block()

    def check_hit(self):

        """"Ici on verifie si le serpent se touche et s'il touche la fenetre de jeu"""
        if not 0 <= self.snake.body[0].x < number or not 0 <= self.snake.body[0].y < number :
            self.game_over()
        for elt in self.snake.body[1:]:
            if self.snake.body[0] == elt:
                self.game_over()

    def game_over(self):
       print("ok")


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
            if event.key == pygame.K_UP and  snake.direction.y != 1:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT and snake.direction.x != -1:
                snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT and snake.direction.x != 1:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_DOWN and snake.direction.y != -1:
                snake.direction = Vector2(0, 1)
    screen.fill((175, 215, 70))
    game.draw_images()
    game.check_collision()
    pygame.display.update()
    clock.tick(60)

pygame.quit()


