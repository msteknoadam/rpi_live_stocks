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
btcLogo = pygame.image.load('bitcoin.png')
usdLogo = pygame.image.load('usd.png')
eurLogo = pygame.image.load('eur.png')

# Initialize some required things for pygame display
DISPLAYSURF = pygame.display.set_mode((X, Y), RESIZABLE)
font = pygame.font.SysFont('Calibri', 40)

# Request URIs to get current stock exchange rates
freecurrencyconverteruri = f"http://free.currconv.com/api/v7/convert?q=%s&compact=ultra&apiKey={freecurrencyconverterapi}"

pygame.display.set_caption("Stocks Watch")

mainLoop = True

while mainLoop:
    print("mainLoop start")
    # I hope I will refactor this one time so user just needs to set an array
    # to define which prices to watch and only add their logos, but meh, soon™
    exchangeRates = requests.get(
        url=freecurrencyconverteruri % "BTC_USD,USD_TRY,EUR_TRY").json()
    btc_usd = exchangeRates["BTC_USD"]
    print(f"BTC - USD Rate: {btc_usd}")
    usd_try = exchangeRates["USD_TRY"]
    print(f"USD - TRY Rate: {usd_try}")
    eur_try = exchangeRates["EUR_TRY"]
    print(f"EUR - TRY Rate: {eur_try}")
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                mainLoop = False
        elif event.type == pygame.QUIT:
            mainLoop = False

    DISPLAYSURF.fill(black)
    timeText = font.render(
        f'Current Time: {int(time.time())}', True, green, black)
    timeTextRect = timeText.get_rect()
    timeTextRect.center = (X // 2, 25)
    btcText = font.render(
        f'BTC-USD: {btc_usd} $', True, green, black)
    btcTextRect = btcText.get_rect()
    btcTextRect.center = ((X // 2) + 75, 100)
    usdText = font.render(
        f'USD-TRY: {usd_try} ₺', True, green, black)
    usdTextRect = usdText.get_rect()
    usdTextRect.center = ((X // 2) + 75, 250)
    eurText = font.render(
        f'EUR-TRY: {eur_try} ₺', True, green, black)
    eurTextRect = eurText.get_rect()
    eurTextRect.center = ((X // 2) + 75, 400)
    DISPLAYSURF.blit(timeText, timeTextRect)
    DISPLAYSURF.blit(btcLogo, (50, 50))
    DISPLAYSURF.blit(usdLogo, (50, 200))
    DISPLAYSURF.blit(eurLogo, (50, 350))
    DISPLAYSURF.blit(btcText, btcTextRect)
    DISPLAYSURF.blit(usdText, usdTextRect)
    DISPLAYSURF.blit(eurText, eurTextRect)
    pygame.display.update()
    pygame.time.delay(10000)

pygame.quit()
