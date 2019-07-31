import pygame
import sys
import time
import requests
from pygame.locals import *
from APIKEYS import freecurrencyconverterapi

pygame.init()

# Global variables
refreshRateInSeconds = 100
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
btc_usd = 0
usd_try = 0
eur_try = 0


# Initialize some required things for pygame display
DISPLAYSURF = pygame.display.set_mode((X, Y), FULLSCREEN)
font = pygame.font.Font('calibri.ttf', 40)

# Request URIs to get current stock exchange rates
freecurrencyconverteruri = f"http://free.currconv.com/api/v7/convert?q=%s&compact=ultra&apiKey={freecurrencyconverterapi}"

pygame.display.set_caption("Stocks Watch")

FETCHPRIECEVENT = pygame.USEREVENT+1
pygame.time.set_timer(FETCHPRIECEVENT, refreshRateInSeconds * 50)


def fetchPrices():
    # I hope I will refactor this one time so user just needs to set an array
    # to define which prices to watch and only add their logos, but meh, soon™
    # Also Python, why do you have to suck? What is this retarded "global" thing??
    global btc_usd
    global usd_try
    global eur_try
    exchangeRates = requests.get(
        url=freecurrencyconverteruri % "BTC_USD,USD_TRY,EUR_TRY").json()
    btc_usd = exchangeRates["BTC_USD"]
    print(f"BTC - USD Rate: {btc_usd}")
    usd_try = exchangeRates["USD_TRY"]
    print(f"USD - TRY Rate: {usd_try}")
    eur_try = exchangeRates["EUR_TRY"]
    print(f"EUR - TRY Rate: {eur_try}")


fetchPrices()


mainLoop = True

while mainLoop:
    for event in pygame.event.get():
        if event.type == FETCHPRIECEVENT:
            fetchPrices()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_ESCAPE):
                mainLoop = False
        elif event.type == pygame.QUIT:
            mainLoop = False

    DISPLAYSURF.fill(black)
    headerText = pygame.font.Font('agency.ttf', 40, bold=1).render(
        'Currency Conversion Rates', True, green, black)
    headerTextRect = headerText.get_rect()
    headerTextRect.center = (X // 2, 15)
    footer = pygame.font.Font('agency.ttf', 20).render(
        'Made with code by TEKNO', True, green, black)
    footerRect = footer.get_rect()
    footerRect.center = (X // 2, 485)
    btcText = font.render(
        f'BTC-USD: {int(btc_usd * 100) / 100} $', True, green, black)
    btcTextRect = btcText.get_rect()
    btcTextRect.center = ((X // 2) + 75, 100)
    usdText = font.render(
        f'USD-TRY: {int(usd_try * 100) / 100} ₺', True, green, black)
    usdTextRect = usdText.get_rect()
    usdTextRect.center = ((X // 2) + 75, 250)
    eurText = font.render(
        f'EUR-TRY: {int(eur_try * 100) / 100} ₺', True, green, black)
    eurTextRect = eurText.get_rect()
    eurTextRect.center = ((X // 2) + 75, 400)
    DISPLAYSURF.blit(headerText, headerTextRect)
    DISPLAYSURF.blit(footer, footerRect)
    DISPLAYSURF.blit(btcLogo, (50, 50))
    DISPLAYSURF.blit(usdLogo, (50, 200))
    DISPLAYSURF.blit(eurLogo, (50, 350))
    DISPLAYSURF.blit(btcText, btcTextRect)
    DISPLAYSURF.blit(usdText, usdTextRect)
    DISPLAYSURF.blit(eurText, eurTextRect)
    pygame.display.update()
    pygame.time.delay(500)

pygame.quit()
