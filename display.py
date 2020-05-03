#!/usr/bin/env python3

import pygame
import sys
import time
import requests
from pygame.locals import *

pygame.init()


def getScaledValue(normalSize):
    return int(normalSize*Y/1080)


# Global variables
infoObject = pygame.display.Info()
refreshRateInSeconds = 100
X = infoObject.current_w
Y = infoObject.current_h
fontSize_big = getScaledValue(100)
fontSize_small = getScaledValue(50)
infoFont_big = pygame.font.Font('agency.ttf', fontSize_big, bold=1)
infoFont_small = pygame.font.Font('agency.ttf', fontSize_small)
currencyFont = pygame.font.Font('calibri.ttf', fontSize_big)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
currencyCount = 4
currencySpacing = (Y - (fontSize_big + 2 * fontSize_small)
                   ) / (currencyCount + 1)
btcLogo = pygame.image.load('bitcoin.png')
usdLogo = pygame.image.load('usd.png')
eurLogo = pygame.image.load('eur.png')
gauLogo = pygame.image.load('gold.png')
btc_usd = 0
usd_try = 0
eur_try = 0
gau_try = 0
errorMessage = ""


# Initialize some required things for pygame display
DISPLAYSURF = pygame.display.set_mode((X, Y), FULLSCREEN)

# Request URIs to get current stock exchange rates (localhost server will be published soon)
currencyConverterApiUrl = f"https://api.tekno.icu/convert?q=%s"

pygame.display.set_caption("Stocks Watch")

FETCHPRIECEVENT = pygame.USEREVENT+1
pygame.time.set_timer(FETCHPRIECEVENT, refreshRateInSeconds * 1000)


def fetchPrices():
    # I hope I will refactor this one time so user just needs to set an array
    # to define which prices to watch and only add their logos, but meh, soon™
    # Also Python, why do you have to suck? What is this retarded "global" thing??
    global btc_usd
    global usd_try
    global eur_try
    global gau_try
    global errorMessage
    exchangeRatesRequest = requests.get(
        url=currencyConverterApiUrl % "btc-usd,usd-try,eur-try,gau-try")
    if exchangeRatesRequest.status_code == 200:
        exchangeRates = exchangeRatesRequest.json()
        print(exchangeRates)
        try:
            btc_usd = float(exchangeRates["btc-usd"])
        except:
            btc_usd = "ERROR"
        try:
            usd_try = float(exchangeRates["usd-try"])
        except:
            usd_try = "ERROR"
        try:
            eur_try = float(exchangeRates["eur-try"])
        except:
            eur_try = "ERROR"
        try:
            gau_try = float(exchangeRates["gau-try"])
        except:
            gau_try = "ERROR"
        errorMessage = ""
    else:
        errorMessage = f"Error. Conversion API Request Status Code: {exchangeRatesRequest.status_code} | {int(time.time())}"
        print(errorMessage)


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
    headerText = infoFont_big.render(
        'Currency Conversion Rates', True, green, black)
    headerTextRect = headerText.get_rect()
    headerTextRect.center = (X // 2, fontSize_big)
    footer = infoFont_small.render(
        'Made with code by TEKNO', True, green, black)
    footerRect = footer.get_rect()
    footerRect.center = (X // 2, Y - fontSize_small)
    if errorMessage != "":
        errfooter = infoFont_small.render(
            errorMessage, True, red, black)
        errfooterRect = errfooter.get_rect()
        errfooterRect.center = (
            X // 2, Y - fontSize_small * 2 - getScaledValue(10))
        DISPLAYSURF.blit(errfooter, errfooterRect)

    try:
        btcText = currencyFont.render(
            f'BTC-USD: {int(btc_usd * 100) / 100} $', True, green, black)
    except:
        btcText = currencyFont.render(f'BTC-USD: ERROR', True, green, black)
    btcTextRect = btcText.get_rect()
    btcTextRect.center = ((X // 2) + getScaledValue(75),
                          fontSize_big + currencySpacing)

    try:
        usdText = currencyFont.render(
            f'USD-TRY: {int(usd_try * 100) / 100} ₺', True, green, black)
    except:
        usdText = currencyFont.render(f'USD-TRY: ERROR', True, green, black)
    usdTextRect = usdText.get_rect()
    usdTextRect.center = ((X // 2) + getScaledValue(75),
                          fontSize_big + currencySpacing * 2)

    try:
        eurText = currencyFont.render(
            f'EUR-TRY: {int(eur_try * 100) / 100} ₺', True, green, black)
    except:
        eurText = currencyFont.render(f'EUR-TRY: ERROR', True, green, black)
    eurTextRect = eurText.get_rect()
    eurTextRect.center = ((X // 2) + getScaledValue(75),
                          fontSize_big + currencySpacing * 3)

    try:
        gauText = currencyFont.render(
            f'GAU-TRY: {int(gau_try * 100) / 100} ₺', True, green, black)
    except:
        gauText = currencyFont.render(f'GAU-TRY: ERROR', True, green, black)
    gauTextRect = gauText.get_rect()
    gauTextRect.center = ((X // 2) + getScaledValue(75),
                          fontSize_big + currencySpacing * 4)

    DISPLAYSURF.blit(headerText, headerTextRect)
    DISPLAYSURF.blit(footer, footerRect)
    DISPLAYSURF.blit(btcText, btcTextRect)
    DISPLAYSURF.blit(usdText, usdTextRect)
    DISPLAYSURF.blit(eurText, eurTextRect)
    DISPLAYSURF.blit(gauText, gauTextRect)
    DISPLAYSURF.blit(btcLogo, (btcTextRect.x - 125, btcTextRect.y - 7.5))
    DISPLAYSURF.blit(usdLogo, (usdTextRect.x - 125, usdTextRect.y - 7.5))
    DISPLAYSURF.blit(eurLogo, (eurTextRect.x - 125, eurTextRect.y - 7.5))
    DISPLAYSURF.blit(gauLogo, (gauTextRect.x - 125, gauTextRect.y - 7.5))
    pygame.display.update()
    pygame.time.delay(500)

pygame.quit()
