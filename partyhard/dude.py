import pygame
from pygame.locals import *

DUDE_IMAGE = "assets/party-dude-155-171.png"

class Dude(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)
    	self.image = pygame.image.load(DUDE_IMAGE)
    	self.rect = self.image.get_rect()
    	self.position = [x_pos, y_pos]

    def moveRight(self):
    	self.position[0] += 5
<<<<<<< HEAD

    def moveLeft(self):
    	self.position[0] -= 5
=======
    	#print "moving right"

    def moveLeft(self):
    	self.position[0] -= 5
    	#print "moving left"
>>>>>>> ca5ed85862ee12a0dc01d97e554897fc5fb6b104
