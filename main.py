from constantes import*
from game import Game
import pygame

pygame.init()

clock = pygame.time.Clock()
run = True
game = Game()

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 150) #indique la vitesse de deplacement du serpent en milliseconde

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
        if event.type == UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            game.update_deplacement(event)

    game.draw_floor()
    game.draw_images()
    game.check_collision()
    game.draw_score()
    pygame.display.update()
    clock.tick(60)