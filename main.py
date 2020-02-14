import pygame
import time
from sprite_handler import rudolphs
from sprite_handler import level_one
from sprite_handler import level_two
from sprite_handler import quit
from sprite_handler import text_to_screen
from sprite_handler import level
from sprite_handler import text_to_button
pygame.init()


background1 = pygame.image.load('textures/bg2.jpg')
background2 = pygame.image.load('textures/bg1.jpg')


black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)


width = 1920
hight = 1080
#the difference between width and hight is 840
run = True
FPS = 60
vel = 1
music_played=0

clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')



def level_maker():
    if level== -1:
        pass



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


def button(text, x, y, width, hight, active_color, inactive_color,size, action = None):
    global level
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + hight > cur[1] > y:
        pygame.draw.rect(window, active_color, (x,y,width,hight))
        if click[2] == 1 and action != None:
            if action == "level1":
                level = 1
            if action == "level2":
                level = 2
            if action == "quit":
                pygame.quit()
                quit()
            if action =="idk":
                pass

    else:
        pygame.draw.rect(window, inactive_color, (x,y,width,hight))
    text_to_button(text,black,x,y,width,hight, size)


def redrawGameWindow():
    if level==1:
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))

    if level==2:
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))

    if level == 0:
        window.blit(pygame.transform.scale(background1, (width,hight)), (0, 0))
        text_to_screen("hi",black,0,0,100,100, "relly_small")
        button("level 1", 860,250, 200,100, red, light_red,"small", action = "level1")
        button("level 2", 860,400, 200,100, red, light_red,"small", action = "level2")
        button("how to play", 860,550, 200,100, yellow, light_yellow,"medium_small", action = "idk",)
        button("Quit", 860,700, 200,100, yellow, light_yellow,"small", action = "quit")


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
quit()
