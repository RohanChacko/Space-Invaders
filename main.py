"""This is the replica of the famous Space Invaders game.
	Created by Rohan Chacko"""

import pygame
from pygame.locals import *
from ships import Ships
from engine import engine
from alien import Inv
from missiles import Missile, Bigmis, Smallmis

pygame.init()

LOOP = True
score = 0

engine.DISP_SCREEN.blit(engine.WALLPAPER, (0, 0))


def finscore(flag=0):
    """Calculates score"""
    global score
    if flag == 1:
        score += 1
    # print(score)
    font = pygame.font.SysFont("monospace", 32)
    score_text = font.render("SCORE: " +
                             str(score), False, (255, 255, 255))
    engine.DISP_SCREEN.blit(score_text, (280, 280))


finscore()

S = Ships()
engine.DISP_SCREEN.blit(engine.SP_SHIP, (S.posx, S.posy))
pygame.display.flip()
I = Inv()
BM = Bigmis()
SM = Smallmis()
pygame.display.flip()


while LOOP:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Handles event when 'X' is pressed
            LOOP = False
        if event.type == KEYDOWN:  # Handles event when 'Q' is pressed

            if event.key == K_a:
                S.move('A')
                I.update()
                finscore()
                pygame.display.flip()

            elif event.key == K_d:
                S.move('D')
                I.update()
                finscore()
                pygame.display.flip()

            elif event.key == K_SPACE:

                xpos, ypos = S.position()
                BM.start(xpos, ypos)
                pygame.display.flip()
                F_TIMER = 6

            elif event.key == K_s:
                xpos, ypos = S.position()
                SM.start(xpos, ypos)
                pygame.display.flip()
                S_TIMER = 2

            elif event.key == K_q:
                LOOP = False

    engine.MAIN_TIMER -= engine.MAIN_CLOCK.tick() / 1000
    engine.F_TIMER -= engine.F_CLOCKMIS.tick(18) / 1000
    engine.S_TIMER -= engine.S_CLOCKMIS.tick(18) / 1000

    if engine.MAIN_TIMER <= 3:

        I.dreate()
        engine.DISP_SCREEN.blit(engine.WALLPAPER, (0, 0))
        finscore()
        I.update()
        S.update()
        pygame.display.flip()

    if engine.MAIN_TIMER <= 0:

        I.create()
        S.update()
        pygame.display.flip()
        engine.MAIN_TIMER = 5

    if engine.F_TIMER <= 6:

        engine.DISP_SCREEN.blit(engine.WALLPAPER, (0, 0))
        finscore()
        BM.update()
        if BM.collision == 1:
            finscore(1)
            BM.collision = 0
        I.update()
        S.update()
        pygame.display.flip()

    if engine.S_TIMER <= 2:

        engine.DISP_SCREEN.blit(engine.WALLPAPER, (0, 0))
        finscore()
        SM.update()
        I.update()
        S.update()
        pygame.display.flip()
