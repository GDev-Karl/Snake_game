import pygame

pygame.mixer.pre_init(444100, -16, 2, 512)
pygame.init()

size = 30
number = 21

screen = pygame.display.set_mode((number * size, number * size))
pygame.display.set_caption(" Snake ")
font_name = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25) #police 
sound = pygame.mixer.Sound('Sound/crunch.wav')