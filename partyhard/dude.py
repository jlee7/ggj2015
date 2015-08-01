import pygame
from pygame.locals import *
import time

#DUDE_IMAGE = "assets/party-dude-155-171.png"
DUDE_SPEED = 20
DUDE_IMAGE = "assets/party-dude.png"
DUDE_IMAGE_RAISED = "assets/party-dude-hands-up.png"
ARMS_RAISED_TICKS = 3

class Dude(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load(DUDE_IMAGE)
    	self.rect = self.image.get_rect()
        self.rect.x = x_pos
    	self.rect.y = y_pos
        self.arms_raised_ticks = 0
        self.arms_raised = False

    def moveRight(self):
    	self.rect.x += DUDE_SPEED

    def moveLeft(self):
    	self.rect.x -= DUDE_SPEED

    def raise_arms(self):
        if not self.arms_raised:
            self.image = pygame.image.load(DUDE_IMAGE_RAISED)
            self.arms_raised = True
            self.arms_raised_ticks = ARMS_RAISED_TICKS

    def lower_arms(self):
        if self.arms_raised:
            if self.arms_raised_ticks > 0:
                self.arms_raised_ticks -= 1
            else:
                self.image = pygame.image.load(DUDE_IMAGE)
                self.arms_raised = False
