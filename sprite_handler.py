import pygame

rudolphs = []

norm_rudolph = pygame.image.load('textures/norm_rudolph.png')
indigo_rudolph = pygame.image.load('textures/indigo_rudolph.png')
turquoise_rudolph = pygame.image.load('textures/turquoise_rudolph.png')
jade_rudolph = pygame.image.load('textures/jade_rudolph.png')
orange_rudolph = pygame.image.load('textures/orange_rudolph.png')

class rudolph0(object):
    def __init__(self, x, y):
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(norm_rudolph, (240,240)), (self.x, self.y))


class rudolph1(object):
    def __init__(self, x, y):
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(indigo_rudolph, (240,240)), (self.x, self.y))


class rudolph2(object):
    def __init__(self, x, y):
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(turquoise_rudolph, (240,240)), (self.x, self.y))


class rudolph3(object):
    def __init__(self, x, y):
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(jade_rudolph, (240,240)), (self.x, self.y))


class rudolph4(object):
    def __init__(self, x, y):
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(orange_rudolph, (240,240)), (self.x, self.y))

