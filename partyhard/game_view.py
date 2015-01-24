import pygame
from items import *
from event_manager import TickEvent

WIDTH = 1024
HEIGHT = 680
DEMOSPRITE_POSITION = [300, 500]

class GameView(object):

    def __init__(self, event_manager):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert()
        self.background.fill((0,255,0))
        self.screen.blit(self.background,(0,0))

        self.demosprite = Item()

        self.itemgroup = pygame.sprite.Group()
        self.itemgroup.add(self.demosprite)        
        self.itemgroup.draw(self.screen)

        #self.screen.blit(self.demosprite.image, DEMOSPRITE_POSITION)

        pygame.display.flip()

    def notify(self, event):
        
        if isinstance(event,TickEvent):

            # falling items
            for item in self.itemgroup:
                item.rect.y += item.fall_speed

            print self.screen
            self.itemgroup.clear(self.screen,self.background)
            self.itemgroup.draw(self.screen)
            pygame.display.flip()


