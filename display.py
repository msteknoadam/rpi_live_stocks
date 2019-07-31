import pygame
import sys
import time
import requests
from pygame.locals import *
from APIKEYS import freecurrencyconverterapi

pygame.init()

# Global variables
X = 500
Y = 500
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# Request URIs to get current stock exchange rates
freecurrencyconverteruri = f"https://free.currencyconverterapi.com/api/v6/convert?q=%s&compact=ultra&apiKey={freecurrencyconverterapi}"
print(freecurrencyconverteruri % "BTC_USD")

DISPLAYSURF = pygame.display.set_mode((X, Y), RESIZABLE)
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.display.set_caption("Stocks Watch")

mainLoop = True

while mainLoop:
    print("mainLoop start")
    pygame.time.delay(2000)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                mainLoop = False
        elif event.type == pygame.QUIT:
            mainLoop = False

    DISPLAYSURF.fill(black)
    text = font.render(f'Current Time: {int(time.time())}', True, green, black)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    DISPLAYSURF.blit(text, textRect)
    pygame.display.update()

pygame.quit()
