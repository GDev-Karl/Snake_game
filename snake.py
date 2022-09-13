import queue
import pygame
from constantes import*
from pygame.math import Vector2

class Snake:

    def __init__(self):

        """ Serpent """
        self.body = [Vector2(3, 10), Vector2(4, 10), Vector2(5, 10)]
        self.direction = Vector2(0, 0) #indique sens de deplacement du serpent (par exemple de la droite vers la gauche)
        self.add = False #indique s'il faut ajouter un block ou pas
        self.snake_images() # ensembles des images necessaires pours dessiner le serpent
        
    def snake_images(self):

        """ initialisation de toutes les images du corps du serpent """

        # differentes positions de la tete
        self.head_up = pygame.image.load('img/head_up.png').convert_alpha()
        self.head_up = pygame.transform.scale(self.head_up, (size, size))

        self.head_down = pygame.image.load('img/head_down.png').convert_alpha()
        self.head_down  = pygame.transform.scale(self.head_down, (size, size))

        self.head_right = pygame.image.load('img/head_right.png').convert_alpha()
        self.head_right  = pygame.transform.scale(self.head_right, (size, size))
        
        self.head_left = pygame.image.load('img/head_left.png').convert_alpha()
        self.head_left = pygame.transform.scale(self.head_left , (size, size))

        #differetes positions du corps
        self.body_vertical = pygame.image.load('img/body_vertical.png').convert_alpha()
        self.body_vertical = pygame.transform.scale(self.body_vertical, (size, size))

        self.body_horizontal = pygame.image.load('img/body_horizontal.png').convert_alpha()
        self.body_horizontal = pygame.transform.scale(self.body_horizontal, (size, size))


        #diffeentes positions da la queue
        self.tail_up = pygame.image.load('img/tail_up.png').convert_alpha()
        self.tail_up = pygame.transform.scale(self.tail_up, (size, size))

        self.tail_down = pygame.image.load('img/tail_down.png').convert_alpha()
        self.tail_down = pygame.transform.scale(self.tail_down, (size, size))

        self.tail_right = pygame.image.load('img/tail_right.png').convert_alpha()
        self.tail_right = pygame.transform.scale(self.tail_right, (size, size))
        
        self.tail_left = pygame.image.load('img/tail_left.png').convert_alpha()
        self.tail_left = pygame.transform.scale(self.tail_left, (size, size))


        #differentes positions du contour
        self.body_br = pygame.image.load('img/body_br.png').convert_alpha()
        self.body_br = pygame.transform.scale(self.body_br, (size, size))

        self.body_bl = pygame.image.load('img/body_bl.png').convert_alpha()
        self.body_bl = pygame.transform.scale(self.body_bl, (size, size))

        self.body_tl = pygame.image.load('img/body_tl.png').convert_alpha()
        self.body_tl = pygame.transform.scale(self.body_tl, (size, size))

        self.body_tr = pygame.image.load('img/body_tr.png').convert_alpha()
        self.body_tr = pygame.transform.scale(self.body_tr, (size, size))

    def draw(self):

        """dessin du serpent"""

        self.update_tail() 
        self.update_head()

        for index, block in enumerate(self.body):
            x = block.x * size
            y = block.y * size
            snake_rect = pygame.Rect(x, y , size, size)

            if index == 0:
                screen.blit(self.tail, snake_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.head, snake_rect)
            else:
                self.update_body(index, block)
                screen.blit(self.pos_body, snake_rect)
    
    def update_head(self):

        """ mise a jour de la position de la tete"""
        if self.direction.x == 1 : # s'il il se dirige vers la droite
            self.head = self.head_right
        elif self.direction.x == 0 and self.body == [Vector2(3, 10), Vector2(4, 10), Vector2(5, 10)]: #position initiale
            self.head = self.head_right
        elif self.direction.x == -1: # s'il il se dirige vers la gauche
            self.head = self.head_left
        elif self.direction.y == 1: # s'il il se dirige vers le bas
            self.head = self.head_down
        elif self.direction.y == -1: # s'il il se dirige vers le haut
            self.head = self.head_up 

    def update_tail(self):

        """ mise a jour de la position de la queue du serpent"""
        direction = self.body[1]  - self.body[0] # elle indique la direction dans laquelle se deplace une partie du corps du serpent la queue et le block qui vient avant la queue
        if direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif direction == Vector2(0, 1):
            self.tail = self.tail_up
        elif direction == Vector2(0, -1):
            self.tail = self.tail_down

    def update_body(self, index, block):

        """ mise a jour de la position du corps du serpent """
        prev_block = self.body[index - 1] - block # sens de la face relier au block precedant 
        next_block = self.body[index + 1] - block # sens de la face relier au block suivant
        after_next_block = self.body[index + 1] # block après le suivant
        direct = after_next_block - next_block
        if prev_block.x == next_block.x: # si le block precedant et le suivant sont alignés suivant x
            self.pos_body = self.body_vertical
        elif prev_block.y == next_block.y: # si le block precedant et le suivant sont alignés suivant y
            self.pos_body = self.body_horizontal
        else:
            if (prev_block.x == -1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == -1):
                self.pos_body = self.body_bl
            elif (prev_block.x == 1 and next_block.y == 1) or (prev_block.y == 1 and next_block.x == 1):
                self.pos_body = self.body_br
            elif (prev_block.x == -1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == -1):
                self.pos_body = self.body_tl
            elif (prev_block.x == 1 and next_block.y == -1) or (prev_block.y == -1 and next_block.x == 1):
                self.pos_body = self.body_tr
            
    def move(self):

        """ deplacement du serpent """
        if self.add:
            sound.play()
            body_copy = self.body[:]
            body_copy.append(body_copy[-1] + self.direction)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[1:] #on recupère tout les éléments de la liste sauf le premier
            body_copy.append(body_copy[- 1] + self.direction)
            self.body = body_copy[:]

    def add_block(self):

        """ ajout d'un nouveau block """
        self.add = True