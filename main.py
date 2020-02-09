import pygame
import time
pygame.init()


rudolph_norm = pygame.image.load('textures/norm_rudof.png')
background = pygame.image.load('textures/bg1.jpg')


width = 1920
hight = 1080
#the difference between width and hight is 840
run = True
FPS = 60
vel = 5
level = 0
rudolph_color = 0
rudolph_place = 0


clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')


class rudolph1(object):
    def __init__(self, x, y):
        self.vel = 20
        self.x = x       
        self.y = y

    def draw(self,window):
        window.blit(pygame.transform.scale(rudolph_norm, (240,240)), (self.x, self.y))


def redrawGameWindow():
    window.blit(pygame.transform.scale(background, (width,hight)), (0, 0))
    for rudolph1 in norm_rudolphs:
        rudolph1.draw(window)

    pygame.display.update()


if run == True:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


norm_rudolphs = []
while run:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False


    for norm_rudolph in norm_rudolphs:
       if norm_rudolph.y < 1080 and norm_rudolph.y > -1:
           norm_rudolph.y += norm_rudolph.vel
        else:
            norm_rudolphs.pop(norm_rudolphs.index(norm_rudolph))


    if len(norm_rudolphs) < 2:
        norm_rudolphs.append(rudolph1(480,0))
        norm_rudolphs.append(rudolph1(0,0))

 
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