import pygame
import time
from sprite_handler import rudolphs
pygame.init()


norm_rudolph = pygame.image.load('textures/norm_rudolph.png')
indigo_rudolph = pygame.image.load('textures/indigo_rudolph.png')
turquoise_rudolph = pygame.image.load('textures/turquoise_rudolph.png')
jade_rudolph = pygame.image.load('textures/jade_rudolph.png')
orange_rudolph = pygame.image.load('textures/orange_rudolph.png')
play = pygame.image.load("textures/lv1.png")
quit = pygame.image.load("textures/quit.png")
two = pygame.image.load("textures/lv2.png")

background2 = pygame.image.load('textures/bg2.jpg')
background = pygame.image.load('textures/bg1.jpg')
overlay1 = pygame.image.load('textures/overlay1.jpg')


width = 1920
hight = 1080
#the difference between width and hight is 840
run = True
FPS = 60
level = 1
vel = 1
music_played=0

clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')



#def level_maker():
    #if level== -1:



def level1():
    global vel
    global music_played
    from level1 import leveldata
    from level1 import vel
    if music_played==0:
        music_played = 1
        music = pygame.mixer.music.load("data/earth.mp3")
        pygame.mixer.music.play(1)
    leveldata()


def level2():
    global vel
    global music_played
    from level2 import leveldata
    from level2 import vel
    if music_played==0:
        music_played = 1
        music = pygame.mixer.music.load("data/earth.mp3")
        pygame.mixer.music.play(1)
    leveldata()



def redrawGameWindow():
    if level==1:
        window.blit(pygame.transform.scale(background, (width,hight)), (0, 0))
    if level == 0:
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        window.blit(pygame.transform.scale(play, (480,240)), (700, 300))
        window.blit(pygame.transform.scale(two, (480,240)), (700, 600))
        window.blit(pygame.transform.scale(quit, (480,240)), (1400, 850))


        

    for rudolph in rudolphs:
        rudolph.draw(window)

    pygame.display.update()


if run == True:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


while run:
    clock.tick(FPS)


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    for rudolph in rudolphs:
        if rudolph.y < 1080 and rudolph.y > -1:
            rudolph.y += vel
        else:
            rudolphs.pop(rudolphs.index(rudolph))

    if level == 1:
        level1()

    if level == 2:
        level2()

    if level < 0:
        level_maker()

 
    redrawGameWindow()


pygame.quit()
