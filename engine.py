"""Engine class"""
import pygame
from pygame.locals import *

class engine(object):

    DISP_SCREEN = pygame.display.set_mode((800, 1080))
    LOOP = True
    MAIN_CLOCK = pygame.time.Clock()
    F_CLOCKMIS = pygame.time.Clock()
    S_CLOCKMIS = pygame.time.Clock()
    MAIN_TIMER = 10
    F_TIMER = 0
    S_TIMER = 0
    score = 0

    WALLPAPER = pygame.image.load("images/bg.png")
    SP_SHIP = pygame.image.load("images/spaceship.png")
    INVADER = pygame.image.load("images/invader.jpg")
    DEAD_INVADER = pygame.image.load("images/deadinvader.jpg")
    B_MISSILE = pygame.image.load("images/mis1.jpg")
    S_MISSILE = pygame.image.load("images/mis2.png")

    WALLPAPER = pygame.transform.scale(WALLPAPER, (1200, 700))
    SP_SHIP = pygame.transform.scale(SP_SHIP, (100, 100))
    INVADER = pygame.transform.scale(INVADER, (100, 100))
    DEAD_INVADER = pygame.transform.scale(DEAD_INVADER, (100, 100))
    B_MISSILE = pygame.transform.scale(B_MISSILE, (90, 90))
    S_MISSILE = pygame.transform.scale(S_MISSILE, (90, 90))

    SP_SHIP.set_colorkey((0, 0, 0))
    INVADER.set_colorkey((0, 0, 0))
    DEAD_INVADER.set_colorkey((0, 0, 0))
    B_MISSILE.set_colorkey((255, 255, 255))
