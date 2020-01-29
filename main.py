import pygame
pygame.init()

WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
GREY = (210, 210 ,210)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)


fullScreen = False
run = True
FPS = 60


clock = pygame.time.Clock()

if run == True:

 if fullScreen == True:
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

 elif fullScreen == False:
    window = pygame.display.set_mode((500, 500))


while run:
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
    clock.tick(FPS)


pygame.quit()
