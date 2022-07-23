import pygame, sys
from pygame.math import Vector2
import random

pygame.mixer.pre_init(444100, -16, 2, 512)
pygame.init()

size = 30
number = 21
clock = pygame.time.Clock()
run = True
screen = pygame.display.set_mode((number * size, number * size))
font_name = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)
sound = pygame.mixer.Sound('Sound/crunch.wav')

class Snake:

    def __init__(self):

        """ Serpent """
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0) #indique la direction de deplacement du serpent
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
                screen.blit(self.head, snake_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, snake_rect)
            else:
                prev_direct = self.body[index + 1] - block #direction du block precedant
                next_direct = self.body[index - 1] - block # direction du block suivant
                if prev_direct.x == next_direct.x: # si le block precedant et le suivant sont alignés suivant x
                    screen.blit(self.body_vertical, snake_rect)
                elif prev_direct.y == next_direct.y: # si le block precedant et le suivant sont alignés suivant y
                    screen.blit(self.body_horizontal, snake_rect)
                else:
                    if (prev_direct.y == 1 and next_direct.x == 1) or (prev_direct.x == 1 and next_direct.y == 1):
                        screen.blit(self.body_br, snake_rect)
                    elif (prev_direct.y == 1 and next_direct.x == -1) or (prev_direct.x == -1 and next_direct.y == 1):
                        screen.blit(self.body_bl, snake_rect)
                    elif (prev_direct.y == -1 and next_direct.x == 1) or (prev_direct.x == 1 and next_direct.y == -1):
                        screen.blit(self.body_tr, snake_rect)
                    elif (prev_direct.y == -1 and next_direct.x == -1) or (prev_direct.x == -1 and next_direct.y == -1):
                        screen.blit(self.body_tl, snake_rect)
                    
        """
            for block in self.body:
            x = block.x * size
            y = block.y * size
            snake_rect = pygame.Rect(x, y , size, size)
            pygame.draw.rect(screen, (123, 123, 156), snake_rect)
        """

    def move(self):

        """ deplacement du serpent """
        if self.add:
            sound.play()
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

    def update_head(self):

        """ mise a jour de la position de la tete"""
        if self.direction.x == 1 : # s'il il se dirige vers la droite
            self.head = self.head_right
        elif self.direction.x == 0 and self.body == [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]: #position initiale
            self.head = self.head_right
        elif self.direction.x == -1: # s'il il se dirige vers la gauche
            self.head = self.head_left
        elif self.direction.y == 1: # s'il il se dirige vers le bas
            self.head = self.head_down
        elif self.direction.y == -1:
            self.head = self.head_up # s'il il se dirige vers le haut

    def update_tail(self):

        """ mise a jour de la position de la queue du serpent"""
        direction = self.body[-2] - self.body[-1] # elle indique la direction dans laquelle se deplace le serpent
        if direction == Vector2(1, 0):
            self.tail = self.tail_left
        elif direction == Vector2(-1, 0):
            self.tail = self.tail_right
        elif direction == Vector2(0, 1):
            self.tail = self.tail_up
        elif direction == Vector2(0, -1):
            self.tail = self.tail_down

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
        
class Main:

    def __init__(self):

        """" classe principale du jeu """
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
 
        """ Verification des collisions entre la pomme et le serpent """
        if self.apple.pos == self.snake.body[0]:
            self.apple.ramdomize()
            self.snake.add_block()

    def check_hit(self):

        """" Ici on verifie si le serpent se touche et s'il touche la fenetre de jeu """
        if not 0 <= self.snake.body[0].x < number or not 0 <= self.snake.body[0].y < number :
            self.game_over()
        for elt in self.snake.body[1:]:
            if self.snake.body[0] == elt:
                self.game_over()

    def draw_floor(self):

        """ dessin du terrain de jeu """
        for row in range(0, 21, 2):
            for col in range(0, 21, 2):
                rect = pygame.Rect(row * size, col * size, size, size)
                pygame.draw.rect(screen, (4, 155, 70), rect)

        for i in range(1, 21, 2):
            for j in range(1, 21, 2):
                rect = pygame.Rect(i * size, j * size, size, size)
                pygame.draw.rect(screen, (4, 155, 70), rect)

    def draw_score(self):

        """ dessin du score """
        score = str(len(snake.body) - 3) # calcul du score
        surface = font_name.render(score, True, (0, 0, 0))
        Apple = pygame.image.load('img/apple.png').convert_alpha()

        x = (size * number) - 60 ; y = (size * number) - 40

        score_rect = surface.get_rect(center = (x, y))
        apple_rect = Apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg = pygame.Rect(apple_rect.left + 10, apple_rect.top + 10, apple_rect.width + score_rect.width + 20 , apple_rect.height + 10) # contour noir qui entoure la pome et le score
        bg.center = apple_rect.midright

        pygame.draw.rect(screen, (0, 0, 0), bg, 2)
        screen.blit(Apple, apple_rect)
        screen.blit(surface, score_rect)
    

    def game_over(self):

        """ fin du jeu """
        self.snake.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.snake.direction = Vector2(0, 0)

    
UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 150) #indique la vitesse de deplacement du serpent en milliseconde
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

    screen.fill((4, 130, 60))
    game.draw_floor()
    game.draw_images()
    game.check_collision()
    game.draw_score()
    pygame.display.update()
    clock.tick(60)

pygame.quit()


