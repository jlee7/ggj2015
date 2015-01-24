'''
Fonts: http://www.nerdparadise.com/tech/python/pygame/basics/part5/
'''

import pygame
from item_sprites import *
from item_models import *
from event_manager import *
from dude import *
from random import randint
from game_sound import *


WIDTH = 1024
HEIGHT = 680
DEMOSPRITE_POSITION = [300, 500]
BACKGROUND_IMAGE = "assets/bg-1.jpg"

#----------------------------------------------------------------------

class GameView(object):

    def __init__(self, event_manager):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.background=pygame.Surface(self.screen.get_size())
        self.background=pygame.image.load(BACKGROUND_IMAGE)
        #self.background=self.background.convert()
        #self.background.fill((0,255,0))
        self.screen.blit(self.background,(0,0))

        #self.demosprite = ItemSprite()

        self.itemgroup = pygame.sprite.Group()
        #self.itemgroup.add(self.demosprite)        
        #self.itemgroup.draw(self.screen)

        self.textgroup = pygame.sprite.Group()

        self.dude = Dude(WIDTH/2,HEIGHT-60)
        self.screen.blit(self.dude.image, self.dude.position)


        #self.screen.blit(self.demosprite.image, DEMOSPRITE_POSITION)

        font = pygame.font.SysFont(None, 72)
        text = font.render("Party Hard!", True, (0, 128, 0))
        #text_position = text.get_rect()

        #self.textgroup.add(text)

        self.screen.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

        pygame.display.flip()

        self.game_sound = GameSound()

        main_track = self.game_sound.load_main_track()
        #main_track.play(-1)

    #---------------------------------------------------------------------- 

    def notify(self, event):
        
        if isinstance(event,TickEvent):

            # falling items
            for item in self.itemgroup:
                item.rect.y += item.fall_speed
                # items falling out of the screen
                if item.rect.y > HEIGHT:
                    item.kill()
                    print "item killed, current items in group: " + str(len(self.itemgroup)) 

            #print self.screen
            self.itemgroup.clear(self.screen,self.background)
            self.itemgroup.draw(self.screen)


            pygame.display.flip()

        elif isinstance(event,SpawnItemEvent):

            if isinstance (event.item, BeerModel):

                beer_sprite = BeerSprite(event.item)
                beer_sprite.rect.x = randint(0,WIDTH)

                self.itemgroup.add(beer_sprite)
                self.itemgroup.draw(self.screen)

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







