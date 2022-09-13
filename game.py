from constantes import*
from apple import Apple
from snake import Snake
from pygame.math import Vector2
import pygame

class Game:

    def __init__(self) -> None:
      self.apple = Apple()
      self.snake = Snake()

    def draw_images(self):

        """ dessine les elements à l'ecran """
        self.apple.draw()
        self.snake.draw()

    def draw_floor(self):

        """ dessin du terrain de jeu """
        for row in range(0, number):
            for col in range(0, number):
                rect = pygame.Rect(row * size, col * size, size, size)
                if (row + col) % 2 == 0:      
                    pygame.draw.rect(screen, (4, 155, 70), rect) #vert foncé
                else:
                    pygame.draw.rect(screen, (4, 130, 60), rect) # vert un peut moins foncé

    def update(self):

        """ met a jour le deplacement du serpent """
        self.snake.move()
        self.check_hit()
       
    def update_deplacement(self, event):

        if event.key == pygame.K_UP and  self.snake.direction.y != 1:
            self.snake.direction = Vector2(0, -1)
        if event.key == pygame.K_RIGHT and self.snake.direction.x != -1:
            self.snake.direction = Vector2(1, 0)
        if event.key == pygame.K_LEFT and self.snake.direction.x != 1:
            self.snake.direction = Vector2(-1, 0)
        if event.key == pygame.K_DOWN and self.snake.direction.y != -1:
            self.snake.direction = Vector2(0, 1)

    def check_collision(self):
 
        """ Verification des collisions entre la pomme et le serpent """
        if self.apple.pos == self.snake.body[-1]:
            self.apple.ramdomize()
            self.snake.add_block()

    def check_hit(self):

        """" Ici on verifie si le serpent se touche et s'il touche la fenetre de jeu """
        if not 0 <= self.snake.body[-1].x < number or not 0 <= self.snake.body[-1].y < number :
            self.game_over()
        for elt in self.snake.body[:-1]:
            if self.snake.body[-1] == elt:
                self.game_over()

    def draw_score(self):

        """ dessin du score """
        score = str(len(self.snake.body) - 3) # calcul du score
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
        self.snake.body = [Vector2(3, 10), Vector2(4, 10), Vector2(5, 10)]
        self.snake.direction = Vector2(0, 0)