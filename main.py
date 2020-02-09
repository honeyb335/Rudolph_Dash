import pygame
pygame.init()

WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


res = 1366,768
run = True
FPS = 60
level = 0
white = (255,255,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))


clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')


background = pygame.image.load('textures/bg1.jpg')


def redrawGameWindow():
    window.blit(pygame.transform.scale(background, (res)), (0, 0))
    pygame.display.update()

if run == True:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while run:
    clock.tick(FPS)
               
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run = False
            
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