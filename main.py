import pygame
import time
from sprite_handler import rudolphs
from sprite_handler import level_one
from sprite_handler import level_two
from sprite_handler import quit
pygame.init()


background1 = pygame.image.load('textures/bg2.jpg')
background2 = pygame.image.load('textures/bg1.jpg')


width = 1920
hight = 1080
#the difference between width and hight is 840
run = True
FPS = 60
level = 0
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
        music = pygame.mixer.music.load("data/Invincible.mp3")
        pygame.mixer.music.play(1)
    leveldata()


def level2():
    global vel
    global music_played
    from level2 import leveldata
    from level2 import vel
    if music_played==0:
        music_played = 1
        music = pygame.mixer.music.load("data/Cartoon.mp3")
        pygame.mixer.music.play(1)
    leveldata()



def redrawGameWindow():
    if level==1:
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))

    if level == 0:
        window.blit(pygame.transform.scale(background1, (width,hight)), (0, 0))
        window.blit(pygame.transform.scale(level_one, (480,240)), (700, 300))
        window.blit(pygame.transform.scale(level_two, (480,240)), (700, 600))
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
