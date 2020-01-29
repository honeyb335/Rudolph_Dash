import pygame
from main import res
pygame.init()

WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

background = pygame.image.load('textures/bg.jpg')
background = pygame.transform.scale(background,(res))
