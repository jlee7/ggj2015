import pygame
from item_sprites import *
from item_models import *
from event_manager import *
from dude import *

WIDTH = 1024
HEIGHT = 680
DEMOSPRITE_POSITION = [300, 500]

#----------------------------------------------------------------------

class GameView(object):

    def __init__(self, event_manager):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.background=pygame.Surface(self.screen.get_size())
        self.background=self.background.convert()
        self.background.fill((0,255,0))
        self.screen.blit(self.background,(0,0))

        self.demosprite = ItemSprite()

        self.itemgroup = pygame.sprite.Group()
        self.itemgroup.add(self.demosprite)        
        self.itemgroup.draw(self.screen)

        self.dude = Dude(WIDTH/2,HEIGHT-60)
        self.screen.blit(self.dude.image, self.dude.position)


        #self.screen.blit(self.demosprite.image, DEMOSPRITE_POSITION)

        pygame.display.flip()

    #---------------------------------------------------------------------- 

    def notify(self, event):
        
        if isinstance(event,TickEvent):

            # falling items
            for item in self.itemgroup:
                item.rect.y += item.fall_speed

            #print self.screen
            self.itemgroup.clear(self.screen,self.background)
            self.itemgroup.draw(self.screen)
            pygame.display.flip()

        elif isinstance(event,SpawnItemEvent):

            if isinstance (event.item, BeerModel):

                print "spawning Beer"

        elif isinstance(event, DudeMoveEvent):
            print "the moves of the dude are in the view!"

            if event.direction == "left":
                print event.direction
                self.dude.moveLeft()
                
            elif event.direction == "right":
                print event.direction
                self.dude.moveRight()



            self.screen.blit(self.background,(0,0))
            self.screen.blit(self.dude.image, self.dude.position)







