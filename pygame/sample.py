import pygame
from pygame.locals import *
pygame.init()


gameScreen = pygame.display.set_mode((600,500))
gameScreen.fill((110,110,5))
pygame.display.flip()

running = True
while(running):
    for event in pygame.event.get():
        if(event.type == QUIT):
            running = False
