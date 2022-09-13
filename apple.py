from constantes import*
from pygame.math import Vector2
import random
import pygame 

class Apple:  

    def __init__(self):

        """ pomme """
        self.ramdomize()

    def draw(self):

        """ Methode permettant de dessiner la pomme """
        apple_rect = pygame.Rect(self.pos.x * size, self.pos.y * size , size, size)
        apple = pygame.image.load('img/apple.png').convert_alpha() # chargement de la pomme
        apple = pygame.transform.scale(apple, (size, size)) #redimensionnement de la pomme
        screen.blit(apple, apple_rect) #dessin de la pomme

    def ramdomize(self):

        """ positionne la pomme au hasard sur le terrain"""
        self.x = random.randint(0, number - 1)
        self.y = random.randint(0, number - 1)
        self.pos = Vector2(self.x, self.y)