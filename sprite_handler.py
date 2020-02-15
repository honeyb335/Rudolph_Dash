import pygame
pygame.init()

rudolphs = []

norm_rudolph = pygame.image.load('textures/norm_rudolph.png')
#indigo_rudolph = pygame.image.load('textures/indigo_rudolph.png')
turquoise_rudolph = pygame.image.load('textures/turquoise_rudolph.png')
jade_rudolph = pygame.image.load('textures/jade_rudolph.png')
orange_rudolph = pygame.image.load('textures/orange_rudolph.png')
level_one = pygame.image.load("textures/lv1.png")
quit = pygame.image.load("textures/quit.png")
level_two = pygame.image.load("textures/lv2.png")


indigo = (75,0,130)
turquoise = (64,224,208)
jade = (0,168,107)
orange = (255,165,0)


black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
light_red = (255,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
green = (34,177,76)
light_green = (0,255,0)


relly_small_font = pygame.font.Font(None, 25)
medium_small_font = pygame.font.Font(None,50)
large_font = pygame.font.Font(None,200)
font = pygame.font.Font(None, 85)
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

level = -1
#color = 1

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

#def color_render():

    #global color

    #if color > 4:
        #color = 1
    #if color == 1:
        #pygame.draw.rect(window,indigo, [1680,0,240,240])
        #pygame.draw.rect(window,indigo, [1200,0,240,240])
        #pygame.draw.rect(window,indigo, [720,0,240,240])
        #pygame.draw.rect(window,indigo, [240,0,240,240])
    #if color == 2:
        #pygame.draw.rect(window,turquoise, [1680,540,240,240])
    #if color == 3:
        #pygame.draw.rect(window,jade, [1680,270,240,240])
    #if color == 4:
        #pygame.draw.rect(window,orange, [1680,810,240,240])

def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = font.render(text, True, color)
    if size == "relly_small":
        textSurface = relly_small_font.render(text, True, color)
    if size == "medium_small":
        textSurface = medium_small_font.render(text, True, color)
    if size == "large":
        textSurface = large_font.render(text, True, color)


    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, button_width, button_hight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx+(button_width/2)), buttony+(button_hight/2))
    window.blit(textSurf, textRect)


def text_to_screen(msg, color, txty, txtx, txt_width, txt_hight, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((txtx+(txt_width/2)), txty+(txt_hight/2))
    window.blit(textSurf, textRect)