import pygame
from pygame.locals import *

DUDE_IMAGE = "assets/party-dude-155-171.png"
DUDE_SPEED = 10

class Dude(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load(DUDE_IMAGE)
    	self.rect = self.image.get_rect()
        self.rect.x = x_pos
    	self.rect.y = y_pos

    def moveRight(self):
    	self.rect.x += DUDE_SPEED

    def moveLeft(self):
    	self.rect.x -= DUDE_SPEED

