import pygame
from pygame.locals import *
import math

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100,100]

player = pygame.image.load("../Idle__000.png")
bg = pygame.image.load("ryloth.jpg")

while 1:
    screen.fill(0)
    screen.blit(bg,(0,0))
    screen.blit(player, playerpos)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True 
            elif event.key == K_s:
                keys[2] = True 
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    elif keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5


