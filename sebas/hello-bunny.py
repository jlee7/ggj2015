#!/usr/bin/env python

# http://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python

import pygame, math
from pygame.locals import *

pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

keys = [False, False, False, False]
playerpos = [100,100]

player = pygame.image.load("../Idle__000.png")
#player = pygame.transform.scale(player, (50,50))
bg = pygame.image.load("ryloth.jpg").convert()

clock = pygame.time.Clock()

step_speed = 5
tick_speed = 15 # framerate

def aspect_scale(img,(bx,by)):
    """ http://pygame.org/pcr/transform_scale/index.php  
    Scales 'img' to fit into box bx/by.
     This method will retain the original image's aspect ratio """
    ix,iy = img.get_size()
    if ix > iy:
        # fit to width
        scale_factor = bx/float(ix)
        sy = scale_factor * iy
        if sy > by:
            scale_factor = by/float(iy)
            sx = scale_factor * ix
            sy = by
        else:
            sx = bx
    else:
        # fit to height
        scale_factor = by/float(iy)
        sx = scale_factor * ix
        if sx > bx:
            scale_factor = bx/float(ix)
            sx = bx
            sy = scale_factor * iy
        else:
            sy = by
    return pygame.transform.scale(img, (int(sx),int(sy)))

def redraw_ninja():
    #screen.fill(0)
    screen.blit(bg,(0,0))
    screen.blit(player, playerpos)
    pygame.display.flip()

def check_events():
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

def move_player():
    global playerpos, redraw
    old_x, old_y = playerpos # needs to be unpacked to break reference
    if keys[0]:
        playerpos[1] -= step_speed
    elif keys[2]:
        playerpos[1] += step_speed
    elif keys[1]:
        playerpos[0] -= step_speed
    elif keys[3]:
        playerpos[0] += step_speed
    if ([old_x, old_y] != playerpos):
        redraw = True

def get_player_angle_to_mouse():
    global playerpos
    position = pygame.mouse.get_pos()
    diff_x = position[1] - (playerpos[1]) 
    diff_y = position[0] - (playerpos[0])
    angle_radians = math.atan2(diff_x, diff_y)
    #angle_degree = math.degrees(angle_radians)
    angle_degree = 360-angle_radians*57.29
    print angle_radians, angle_degree
    return angle_degree

def rotate_player(degrees):
    global playerpos, player, redraw
    old_x, old_y = playerpos
    playerrot = pygame.transform.rotate(player, degrees)
    playerpos_new_x = old_x - playerrot.get_rect().width/2
    playerpos_new_y = old_y - playerrot.get_rect().height/2
    playerpos1 = [playerpos_new_x, playerpos_new_y]
    #print player, [old_x, old_y], playerpos

    screen.blit(playerrot, playerpos1) 


player = aspect_scale(player, (120,120))

#redraw_ninja()

while True:

    clock.tick(tick_speed)
    screen.fill(0)
    redraw = False

    rotate_player(get_player_angle_to_mouse())

    check_events()

    move_player()

    pygame.display.flip()


    





