import pygame
import time
pygame.init()


norm_rudolph = pygame.image.load('textures/norm_rudolph.png')
indigo_rudolph = pygame.image.load('textures/indigo_rudolph.png')
turquoise_rudolph = pygame.image.load('textures/turquoise_rudolph.png')
jade_rudolph = pygame.image.load('textures/jade_rudolph.png')
orange_rudolph = pygame.image.load('textures/orange_rudolph.png')

background = pygame.image.load('textures/bg1.jpg')


width = 1920
hight = 1080
#the difference between width and hight is 840
run = True
FPS = 60
level = 0
vel = 1

clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')


class rudolph0(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(norm_rudolph, (240,240)), (self.x, self.y))


class rudolph1(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(indigo_rudolph, (240,240)), (self.x, self.y))


class rudolph2(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(turquoise_rudolph, (240,240)), (self.x, self.y))


class rudolph3(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(jade_rudolph, (240,240)), (self.x, self.y))


class rudolph4(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(orange_rudolph, (240,240)), (self.x, self.y))

#def level1:


def redrawGameWindow():
    window.blit(pygame.transform.scale(background, (width,hight)), (0, 0))
    for rudolph in rudolphs:
        rudolph.draw(window)

    pygame.display.update()


if run == True:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


rudolphs = []
while run:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False


    for rudolph in rudolphs:
       if rudolph.y < 1080 and rudolph.y > -1:
           rudolph.y += rudolph.vel
       else:
            rudolphs.pop(rudolphs.index(rudolph))


    if len(rudolphs) < 1:
        rudolphs.append(rudolph4(1440,0))
        rudolphs.append(rudolph3(960,0))
        rudolphs.append(rudolph2(480,0))
        rudolphs.append(rudolph1(0,0))

 
    redrawGameWindow()


pygame.quit()
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)