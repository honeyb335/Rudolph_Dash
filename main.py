import pygame
import time
from sprite_handler import rudolphs
from sprite_handler import level_one
from sprite_handler import level_two
from sprite_handler import quit
from sprite_handler import text_to_screen
from sprite_handler import level
from sprite_handler import text_to_button
from sprite_handler import norm_rudolph
#from sprite_handler import color_render
#from sprite_handler import color
pygame.init()


background1 = pygame.image.load('textures/bg2.jpg')
background2 = pygame.image.load('textures/bg1.jpg')
background3 = pygame.image.load('textures/bg3.jpg')


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
noGood = 0
youGood = 0
score = 0
miss = 0

clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')



def level_maker():
    if level== -1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN and level > 0:
                start = time.time()

                if event.key == pygame.K_a:
                    with open('level1.txt','a') as f:
                        f.write(        rudolphs.append(rudolph4(0,0)))
                        stop = time.time()
                        together = (stop-start)
                        f.write(        time.sleep(stop))
                        print('button')

                if event.key == pygame.K_s:
                    pass

                if event.key == pygame.K_d:
                    pass

                if event.key == pygame.K_f:
                    pass

                if event.key == pygame.K_j:
                    pass
            
                if event.key == pygame.K_k:
                    pass
        
                if event.key == pygame.K_l:
                    pass
            
                if event.key == pygame.K_SEMICOLON:
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
    global score
    global music_played
    global rudolphs
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cur[0] > x and y + hight > cur[1] > y:
        pygame.draw.rect(window, active_color, (x,y,width,hight))
        if click[0] == 1 and action != None:
            if action == "level1":
                level = -10
            if action == "level2":
                level = -20
            if action == "quit":
                pygame.quit()
            if action =="idk":
                level = -5
                music = pygame.mixer.music.load("data/voice.mp3")
                pygame.mixer.music.play(1)
            if action =="back":
                level = 0
                score = 0
                pygame.mixer.music.stop()
                music_played = 0


    else:
        pygame.draw.rect(window, inactive_color, (x,y,width,hight))
    text_to_button(text,black,x,y,width,hight, size)


def redrawGameWindow():
    global youGood
    global noGood
    global miss
    global level
    if level == -5:
        window.blit(pygame.transform.scale(background3, (width,hight)), (0, 0))
        text_to_screen('Hi! XD',black,85,0,1920,0,"medium_small")
        text_to_screen('Welcome to Rudolph Dash',black,255,0,1920,0,"medium_small")
        text_to_screen('Rest your fingers on home row. These are keys "asdf" for the left hand and "jkl;" for the right hand.',black,340,0,1920,0,"medium_small")
        text_to_screen('As Rudolph runs down the screen, press the corresponding keys when Rudolph',black,425,0,1920,0,"medium_small")
        text_to_screen('falls in between the black horizontal lines.',black,510,0,1920,0,"medium_small")
        text_to_screen('Points will be awarded for accuracy and deducted for inaccuracy.',black,595,0,1920,0,"medium_small")
        text_to_screen('A miss will result when Rudolph falls off the screen and has higher deductions.',black,680,0,1920,0,"medium_small")
        text_to_screen('Music used by permision from NCS',black,850,0,1920,0,"medium_small")
        text_to_screen('https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg',black,935,0,1920,0,"medium_small")
        button("Back",1720,0, 200,100, yellow, light_yellow,"small", action = "back")

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
    if level > 0:
        text_to_screen("A",black,800,60, 100,100, "large")
        text_to_screen("S",black,800,300, 100,100, "large")
        text_to_screen("D",black,800,540, 100,100, "large")
        text_to_screen("F",black,800,780, 100,100, "large")
        text_to_screen("J",black,800,1020, 100,100, "large")
        text_to_screen("K",black,800,1260, 100,100, "large")
        text_to_screen("L",black,800,1500, 100,100, "large")
        text_to_screen(";",black,800,1740, 100,100, "large")
        button("Back",1720,0, 200,100, yellow, light_yellow,"small", action = "back")

    if level == -10:
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("A",black,800,60, 100,100, "large")
        text_to_screen("S",black,800,300, 100,100, "large")
        text_to_screen("D",black,800,540, 100,100, "large")
        text_to_screen("F",black,800,780, 100,100, "large")
        text_to_screen("J",black,800,1020, 100,100, "large")
        text_to_screen("K",black,800,1260, 100,100, "large")
        text_to_screen("L",black,800,1500, 100,100, "large")
        text_to_screen(";",black,800,1740, 100,100, "large")
        button("Back",1720,0, 200,100, yellow, light_yellow,"small", action = "back")
        pygame.display.update()
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("3",green,540,960,50,50,"large")
        pygame.display.update()
        time.sleep(1)
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("2",yellow,540,960,50,50,"large")
        pygame.display.update()
        time.sleep(1)
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("1",red,540,960,50,50,"large")
        pygame.display.update()
        time.sleep(1)
        level = 1

    if level == -20:
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("A",black,800,60, 100,100, "large")
        text_to_screen("S",black,800,300, 100,100, "large")
        text_to_screen("D",black,800,540, 100,100, "large")
        text_to_screen("F",black,800,780, 100,100, "large")
        text_to_screen("J",black,800,1020, 100,100, "large")
        text_to_screen("K",black,800,1260, 100,100, "large")
        text_to_screen("L",black,800,1500, 100,100, "large")
        text_to_screen(";",black,800,1740, 100,100, "large")
        button("Back",1720,0, 200,100, yellow, light_yellow,"small", action = "back")
        pygame.display.update()
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("3",green,540,960,50,50,"large")
        pygame.display.update()
        time.sleep(1)
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("2",yellow,540,960,50,50,"large")
        pygame.display.update()
        time.sleep(1)
        window.blit(pygame.transform.scale(background2, (width,hight)), (0, 0))
        text_to_screen("1",red,540,960,50,50,"large")
        pygame.display.update()
        time.sleep(1)
        level = 2

    for rudolph in rudolphs:
        rudolph.draw(window)
    if level > 0:
        score_font = pygame.font.Font(None,85)
        score_surf = score_font.render(str(score),1,black)
        score_pos = [0,0]
        window.blit(score_surf, score_pos)

    if noGood > 0:
        text_to_screen("No Good :|",yellow, 600,800,100,100)
        noGood = noGood + 1
    if noGood > 10:
        noGood = 0

    if youGood > 0:
        text_to_screen("You Good :)",green, 600,800,100,100)
        youGood = youGood + 1
    if youGood > 10:
        youGood = 0

    if miss > 0:
        text_to_screen("miss :(",red, 600,800,100,100)
        miss = miss + 1
    if miss > 10:
        miss = 0


    pygame.display.update()


if run == True:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


while run:
    clock.tick(FPS)


    for event in pygame.event.get():
        if level== -1:
            start = time.time()
            if event.type == pygame.KEYDOWN:
            

                if event.key == pygame.K_a:
                    with open('level1.txt','a') as f:
                        stop = time.time()
                        together = (stop-start)
                        f.write(f"        time.sleep({together})\n")
                        f.write("        rudolphs.append(rudolph4(0,0))\n")
                        print('button')
                        start = time.time()

                if event.key == pygame.K_s:
                    pass

                if event.key == pygame.K_d:
                    pass

                if event.key == pygame.K_f:
                    pass

                if event.key == pygame.K_j:
                    pass
            
                if event.key == pygame.K_k:
                    pass
        
                if event.key == pygame.K_l:
                    pass
            
                if event.key == pygame.K_SEMICOLON:
                    pass
        if event.type == pygame.KEYDOWN and level > 0:
            for rudolph in rudolphs:

                if event.key == pygame.K_a:
                    if rudolph in rudolphs and rudolph.x == 0 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 0 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))

                if event.key == pygame.K_s:
                    if rudolph in rudolphs and rudolph.x == 240 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 240 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))

                if event.key == pygame.K_d:
                    if rudolph in rudolphs and rudolph.x == 480 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 480 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))

                if event.key == pygame.K_f:
                    if rudolph in rudolphs and rudolph.x == 720 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 720 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))

                if event.key == pygame.K_j:
                    if rudolph in rudolphs and rudolph.x == 960 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 960 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))
            
                if event.key == pygame.K_k:
                    if rudolph in rudolphs and rudolph.x == 1200 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 1200 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))
            
                if event.key == pygame.K_l:
                    if rudolph in rudolphs and rudolph.x == 1440 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 1440 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))
            
                if event.key == pygame.K_SEMICOLON:
                    if rudolph in rudolphs and rudolph.x == 1680 and 650 <= rudolph.y <= 800:
                        print("you good")
                        youGood = 1
                        score = score + 10
                        rudolphs.pop(rudolphs.index(rudolph))
                    
                    elif rudolph in rudolphs and rudolph.x == 1680 and rudolph.y < 649:
                        print("no good")
                        noGood = 1
                        score = score - 15
                        rudolphs.pop(rudolphs.index(rudolph))


        if event.type==pygame.QUIT:
            run = False

    for rudolph in rudolphs:
        if rudolph.y < 801 and rudolph.y > -1:
            rudolph.y += vel
        else:
            rudolphs.pop(rudolphs.index(rudolph))
            miss = 1
            score = score -25


    if level == 1:
        level1()

    if level == 2:
        level2()

    #if level < 0:
        #level_maker()

    if level == 0:
        for rudolph in rudolphs:
            rudolphs.pop(rudolphs.index(rudolph))

 
    redrawGameWindow()


pygame.quit()
quit()
