import pygame
import sys
from pygame.locals import *

pygame.init()

X = 500
Y = 500

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Create a displace surface object
# Below line will let you toggle from maximize to the initial size
DISPLAYSURF = pygame.display.set_mode((X, Y), RESIZABLE)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Hello World', True, green, black)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)

pygame.display.set_caption("Stocks Watch")

mainLoop = True

while mainLoop:
    pygame.time.delay(500)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                mainLoop = False
        elif event.type == pygame.QUIT:
            mainLoop = False

    DISPLAYSURF.fill((0, 0, 0))
    DISPLAYSURF.blit(text, textRect)
    pygame.display.update()

pygame.quit()
