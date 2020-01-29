import pygame
pygame.init()

WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


res = 1920,1080
run = True
FPS = 60


clock = pygame.time.Clock()
pygame.display.set_caption('Rudolph Dash')


background = pygame.image.load('textures/bg.jpg')
background = pygame.transform.scale(background,(res))



def redrawGameWindow():
    window.blit(background, (0,0))
    pygame.display.update()

if run == True:
    #window = pygame.display.set_mode((res))
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

while run:
    clock.tick(FPS)
               
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            run = False
            
    redrawGameWindow()


pygame.quit()
