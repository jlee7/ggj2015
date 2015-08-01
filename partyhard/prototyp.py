import pygame
from pygame.locals import *


pygame.init()

WIDTH = 1024
HEIGHT = 680


screen = pygame.display.set_mode((WIDTH, HEIGHT))

DUDE = pygame.image.load("assets/dummy.png")
keys = [False, False, False, False]
DUDE_POSITION = [300, 500]

while True:
    screen.fill(0)
    screen.blit(DUDE, DUDE_POSITION)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                keys[0]=True
            elif event.key==K_a:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_w:
                keys[0]=False
            elif event.key==pygame.K_a:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False
    if keys[0]:
        DUDE_POSITION[1] -= 1
    elif keys[2]:
        DUDE_POSITION[1] += 1
    if keys[1]:
        DUDE_POSITION[0] -= 1
    elif keys[3]:
        DUDE_POSITION[0] += 1

    pygame.display.flip()