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

        # injects
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.game_model = game_model
        # basic screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background=pygame.Surface(self.screen.get_size())
        self.background=pygame.image.load(BACKGROUND_IMAGE)
        self.screen.blit(self.background,(0,0))
        # basic text
        self.game_text = GameText()
        self.text_score = self.game_text.get_score_text(self.game_model.score)

        self.mode_text1 = self.game_text.get_announce_text1()
        self.mode_text2 = self.game_text.get_announce_text2()


        self.textlist = [self.text_score]
        self.modelist = [self.mode_text1, self.mode_text2]

        self.itemgroup = pygame.sprite.Group()
        self.textgroup = pygame.sprite.Group()
        # dude
        self.dude = Dude(WIDTH/2,HEIGHT-172)
        self.screen.blit(self.dude.image, (self.dude.rect.x,self.dude.rect.y))
        # draw
        pygame.display.flip()
        # sound
        self.game_sound = GameSound()
        main_track = self.game_sound.load_main_track()
        #main_track.play(-1)

    #---------------------------------------------------------------------- 

    def notify(self, event):
        
        if isinstance(event,TickEvent):

            # falling items
            for item in self.itemgroup:
                item.rect.y += item.fall_speed
                if item.rect.y > HEIGHT: # items falling out of the screen
                    item.kill()

                    self.game_model.score += 1 
                    self.textlist.remove(self.text_score)
                    self.text_score = self.game_text.get_score_text(self.game_model.score)
                    self.textlist.append(self.text_score)

            # colliding items
            collided_item = pygame.sprite.spritecollideany(self.dude, self.itemgroup)
            if collided_item:
                self.event_manager.post(CollisionEvent(collided_item))
                collided_item.kill()

            # DRAW SHIT
            self.update_screen()


        elif isinstance(event,SpawnItemEvent):

            if isinstance (event.item, BeerModel):
                sprite = BeerSprite(event.item)
            elif isinstance (event.item, CocktailModel):
                sprite = CocktailSprite(event.item)
            elif isinstance (event.item, BookModel):
                sprite = BookSprite(event.item)
            elif isinstance (event.item, PenModel):
                sprite = PenSprite(event.item)

            if sprite:
                sprite.rect.x = randint(0,WIDTH)
                self.itemgroup.add(sprite)

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
        #Punkteanzeige
        for text in self.textlist:
            self.screen.blit(text,(0,0))
        #Modusanzeige
        #for text in self.modelist:
        #    self.screen.blit(text, (700,0))

        self.screen.blit(self.modelist[0], (700,0))
        pygame.display.flip()



class GameText(object):

    def __init__(self):

        self.font_big = pygame.font.SysFont(None, 72)
        self.font_score = pygame.font.SysFont(None, 44)

    def get_score_text(self, score):
        score_text = self.font_score.render("Score: " + str(score), True, (0, 128, 0))
        #print score_text
        return score_text

    def get_announce_text1(self):
        return self.font_big.render("Party Hard!", True, (0, 128, 0))

    def get_announce_text2(self):
        return self.font_big.render("Study Time!", True, (0, 128, 0))


