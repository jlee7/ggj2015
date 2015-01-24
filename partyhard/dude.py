import pygame
from pygame.locals import *

class Dude(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load("assets/dummy.png")
    	self.rect = self.image.get_rect()
    	self.position = [x_pos, y_pos]

    def moveRight():
    	self.rect.x += 3

    def moveLeft():
    	self.rect.x -= 3
