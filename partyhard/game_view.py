import pygame
from items import *

WIDTH = 1024
HEIGHT = 680
DEMOSPRITE_POSITION = [300, 500]

class GameView(object):

    def __init__(self, event_manager):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.demosprite = Item()

        self.itemgroup = pygame.sprite.Group()
        self.itemgroup.add(self.demosprite)        
        self.itemgroup.draw(self.screen)

        #self.screen.blit(self.demosprite.image, DEMOSPRITE_POSITION)

        pygame.display.flip()



    def notify(self, event):
        pass

