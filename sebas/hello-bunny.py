import pygame, math
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100,100]

player = pygame.image.load("../Idle__000.png")
bg = pygame.image.load("ryloth.jpg").convert()

clock = pygame.time.Clock()

step_speed = 5

def redraw_ninja():
    screen.fill(0)
    screen.blit(bg,(0,0))
    screen.blit(player, playerpos)
    pygame.display.flip()

redraw_ninja()

while True:

    clock.tick(120)

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
        playerpos[1] -= step_speed
        redraw_ninja()
    elif keys[2]:
        playerpos[1] += step_speed
        redraw_ninja()
    elif keys[1]:
        playerpos[0] -= step_speed
        redraw_ninja()
    elif keys[3]:
        playerpos[0] += step_speed
        redraw_ninja()



