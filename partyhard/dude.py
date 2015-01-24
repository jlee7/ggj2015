import pygame
from pygame.locals import *

DUDE_IMAGE = "assets/dummy.png"

class Dude(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load(DUDE_IMAGE)
    	self.rect = self.image.get_rect()
    	self.position = [x_pos, y_pos]

    def moveRight(self):
    	self.position[0] += 5
    	print "moving right"

    def moveLeft(self):
    	self.position[0] -= 5
    	print "moving left"
