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

    def __init__(self, event_manager, game_model):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)

        self.game_model = game_model

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        self.background=pygame.Surface(self.screen.get_size())
        self.background=pygame.image.load(BACKGROUND_IMAGE)
        #self.background=self.background.convert()
        #self.background.fill((0,255,0))
        self.screen.blit(self.background,(0,0))

        #self.demosprite = ItemSprite()

        self.game_text = GameText()

        #self.textdict = {'score' : self.game_text.get_score_text()}

        self.text_score = self.game_text.get_score_text(self.game_model.score)

        self.textlist = [self.text_score]

        self.itemgroup = pygame.sprite.Group()
        #self.itemgroup.add(self.demosprite)        
        #self.itemgroup.draw(self.screen)


        self.textgroup = pygame.sprite.Group()

        self.dude = Dude(WIDTH/2,HEIGHT-172)

        self.screen.blit(self.dude.image, (self.dude.rect.x,self.dude.rect.y))

        #self.screen.blit(self.demosprite.image, DEMOSPRITE_POSITION)

        #text_position = text.get_rect()

        #self.textgroup.add(text)


        #self.screen.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))

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
                    print item, "gone"
                    item.kill()
                    #print "item killed, current items in group: " + str(len(self.itemgroup)) 
                
                    self.game_model.score += 1 
                    #print "game model score: " + str(self.game_model.score)
                    self.textlist.remove(self.text_score)
                    self.text_score = self.game_text.get_score_text(self.game_model.score)
                    self.textlist.append(self.text_score)

            collision = pygame.sprite.spritecollideany(self.dude, self.itemgroup)

            if collision:
                print self.dude.rect, collision.rect
                #remove_list = []
                #remove_list.append(collision)
                collision.kill()
                print collision , "killed"
                #for thing in remove_list:
                #    self.itemgroup.remove(thing)

            #print self.screen
            # self.itemgroup.clear(self.screen,self.background)
            self.update_screen()


        elif isinstance(event,SpawnItemEvent):

            if isinstance (event.item, BeerModel):

                beer_sprite = BeerSprite(event.item)
                beer_sprite.rect.x = randint(0,WIDTH)

                self.itemgroup.add(beer_sprite)
                #self.itemgroup.draw(self.screen)

        elif isinstance(event, DudeMoveEvent):

            if event.direction == "left":
                #print event.direction
                self.dude.moveLeft()
                
            elif event.direction == "right":
                #print event.direction
                self.dude.moveRight()

    def display_announce_text(self):
        pass

    def update_screen(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.dude.image, (self.dude.rect.x,self.dude.rect.y))
        self.itemgroup.draw(self.screen) 
        for text in self.textlist:
            self.screen.blit(text,(0,0))
        pygame.display.flip()



class GameText(object):

    def __init__(self):

        self.font_big = pygame.font.SysFont(None, 72)
        self.font_score = pygame.font.SysFont(None, 44)

    def get_score_text(self, score):
        score_text = self.font_score.render("Score: " + str(score), True, (0, 128, 0))
        print score_text.image
        #print score_text
        return score_text

    def get_announce_text(self):
        return self.font_big.render("Party Hard!", True, (0, 128, 0))


