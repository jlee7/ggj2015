import pygame
import random
from item_sprites import *
from item_models import *
from event_manager import *
from dude import *
from random import randint
from game_sound import *
from game_model import *


WIDTH = 1024
HEIGHT = 680
DEMOSPRITE_POSITION = [300, 500]
BACKGROUND_PARTYTIME = "assets/bg-1.jpg"
BACKGROUND_STUDYTIME = "assets/bg-2.jpg"

#----------------------------------------------------------------------

class GameView(object):

    first_startup = True

    def __init__(self, event_manager, game_model, time_controller):

        # injects
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.game_model = game_model
        self.time_controller = time_controller
        # flags
        self.game_over_screen = False
        self.game_start_screen = False
        self.partytime = True # man braucht hier leider ein eigenen party time flag
        # basic screen
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.background=pygame.Surface(self.screen.get_size())
        # Background image depending on mode
        if self.partytime == True:
            self.background=pygame.image.load(BACKGROUND_PARTYTIME)
        else:
            self.background=pygame.image.load(BACKGROUND_STUDYTIME)
        self.screen.blit(self.background,(0,0))
        # basic text
        self.game_text = GameText()
        self.text_score = self.game_text.get_score_text(self.game_model.score)
        self.text_time = self.game_text.get_time(self.time_controller.get_countdown_time)

        self.mode_text1 = self.game_text.get_announce_text1()
        self.mode_text2 = self.game_text.get_announce_text2()
        self.textlist = [self.text_score]
        ###self.timelist = [self.time_text]
        self.modelist = [self.mode_text1, self.mode_text2]
        self.modetext = self.modelist[0]
        # groups
        self.itemgroup = pygame.sprite.Group()
        self.textgroup = pygame.sprite.Group()
        self.killgroup = pygame.sprite.Group()
        # dude
        self.dude = Dude(WIDTH/2,HEIGHT-172)
        self.screen.blit(self.dude.image, (self.dude.rect.x,self.dude.rect.y))
        # draw
        pygame.display.flip()
        # sound - tracks
        self.game_sound = GameSound()
        self.party_track = self.game_sound.load_party_track()
        self.party_track.play(-1)
        self.study_track = self.game_sound.load_study_track()
        self.game_paused_track = self.game_sound.load_game_paused_track()
        # sound - action sounds
        self.sound_mmmh = self.game_sound.load_sound_mmmh()
        self.sound_no = self.game_sound.load_sound_no()
        self.sound_no2 = self.game_sound.load_sound_no2()
        self.sound_partyhard = self.game_sound.load_sound_partyhard()
        self.sound_partytime = self.game_sound.load_sound_partytime()
        self.sound_studytime = self.game_sound.load_sound_studytime()
        self.sound_whatdowedonow = self.game_sound.load_sound_whatdowedonow()
        self.sound_yeah = self.game_sound.load_sound_yeah()
        # flags
        self.game_over_screen = False
        self.partytime = True # man braucht hier leider ein eigenen party time flag
        # parameters
        self.item_fall_speed_modifier_partytime = 1.0
        self.item_fall_speed_modifier_studytime = 1.6
        self.item_fall_speed_modifier_factor = 1.3
        self.item_fall_speed_modifier = self.item_fall_speed_modifier_partytime
        # Startup
        if self.first_startup:
            self.show_startup()
        # draw
        pygame.display.flip()

    #---------------------------------------------------------------------- 

    def notify(self, event):
        
        # Ticker Event
        if isinstance(event,TickEvent):
            if self.game_model.state is not GameModel.STATE_PAUSED:  

                # kill collided items with delay
                for item in self.killgroup:
                    item.kill_try()

                # falling items
                for item in self.itemgroup:
                    item.rect.y += item.fall_speed * self.item_fall_speed_modifier
                    if item.rect.y > HEIGHT: # items falling out of the screen
                        item.kill()

                # colliding items
                collided_item = pygame.sprite.spritecollideany(self.dude, self.itemgroup)
                if collided_item and not collided_item.collided:
                    collided_item.collide(self.partytime)
                    self.event_manager.post(CollisionEvent(collided_item.item_model))
                    self.dude.raise_arms()
                    self.update_score()
                    #self.itemgroup.remove(collided_item)
                    self.killgroup.add(collided_item)
                    #collided_item.kill()
                else:
                    self.dude.lower_arms()   

                # DRAW SHIT      
                self.update_screen()

            elif not self.game_over_screen and not self.game_start_screen:
                self.show_game_over()
                self.game_over_screen = True
            self.update_time()


        # Spawn Event
        elif isinstance(event,SpawnItemEvent):
            if isinstance (event.item, BeerModel):
                sprite = BeerSprite(event.item, self.partytime)
            elif isinstance (event.item, CocktailModel):
                sprite = CocktailSprite(event.item, self.partytime)
            elif isinstance (event.item, BookModel):
                sprite = BookSprite(event.item, self.partytime)
            elif isinstance (event.item, PenModel):
                sprite = PenSprite(event.item, self.partytime)
            if sprite:
                sprite.rect.x = randint(0,WIDTH)
                self.itemgroup.add(sprite)

        # Move Event
        elif isinstance(event, DudeMoveEvent):
            if event.direction == "left":
                #print event.direction
                self.dude.moveLeft()
            elif event.direction == "right":
                #print event.direction
                self.dude.moveRight()

        # Toggle Party Time
        elif isinstance(event, PartyTimeSwitch):

            self.flip_partytime()

            if self.partytime == True:
                self.background = pygame.image.load(BACKGROUND_PARTYTIME)
                self.modetext = self.modelist[0]
                self.study_track.stop()
                self.party_track.play(-1)
                self.sound_partytime.play()
                self.item_fall_speed_modifier = self.item_fall_speed_modifier_partytime
                self.item_fall_speed_modifier_studytime = (self.item_fall_speed_modifier_studytime 
                                                            * self.item_fall_speed_modifier_factor)
            else:
                self.background = pygame.image.load(BACKGROUND_STUDYTIME)
                self.modetext = self.modelist[1]
                self.party_track.stop()
                self.study_track.play(-1)
                self.sound_studytime.play()
                self.item_fall_speed_modifier = self.item_fall_speed_modifier_studytime
            self.itemgroup.update(self.partytime)

        # Restart Game    
        elif isinstance(event, RestartGameEvent):
            self.game_sound.stop_all_sounds()
            self.__init__(self.event_manager, self.game_model, self.time_controller)
            print "GameView: restart game"


        # Game Over
        elif isinstance(event, StopGameEvent):
            self.game_sound.stop_all_sounds()
            self.game_paused_track.play(-1)

        elif isinstance(event, ItemCatchPositive):
            self.sound_yeah.play()

        elif isinstance(event, ItemCatchNegative):
            randomnumber = random.randrange(0,3)
            #print randomnumber
            if randomnumber == 0:
                self.sound_no.play()
            elif randomnumber == 1:
                self.sound_no2.play()
            elif randomnumber == 2:
                self.sound_mmmh.play()

    def show_startup(self):
        self.party_track.stop()
        self.game_paused_track.play(-1)
        self.game_model.state = GameModel.STATE_PAUSED
        game_start_sprite = pygame.sprite.Sprite()
        game_start_sprite.image = pygame.image.load("assets/Splash-Screen.png")
        self.screen.blit(game_start_sprite.image,(0,0))
        self.game_start_screen = True
        self.first_startup = False

    def flip_partytime(self):
        if self.partytime == True:
            self.partytime = False
        else:
            self.partytime = True

    def display_announce_text(self):
        pass

    def update_score(self):
        self.textlist.remove(self.text_score)
        self.text_score = self.game_text.get_score_text(self.game_model.score)
        self.textlist.append(self.text_score)

    def update_time(self):
        self.text_time = self.game_text.get_time(self.time_controller.get_countdown_time())


    def show_game_over(self):

        '''
        # Text
        text_game_over_headline = self.game_text.get_game_over_headline()
        box.blit(text_game_over_headline, (0, 0))
        '''
        game_over_sprite = pygame.sprite.Sprite()
        game_over_sprite.image = pygame.image.load("assets/End-Screen.png")
        self.textlist.remove(self.text_score)
        # Draw
        self.screen.blit(game_over_sprite.image,(0,0))

        pygame.display.flip()

    def update_screen(self):

        box = pygame.Surface((1024,75))
        box.set_alpha(128)
        box.fill((0, 0, 0))
        
        self.screen.blit(self.background,(0,0))


        self.screen.blit(self.dude.image, (self.dude.rect.x,self.dude.rect.y))
        self.itemgroup.draw(self.screen)
        self.screen.blit(box, (0, 0))
        #Punkteanzeige
        for text in self.textlist:
            self.screen.blit(text,(20,20))
        #Modusanzeige
        self.screen.blit(self.modetext, (720, 0))
        self.screen.blit(self.text_time, (400, 20))

        #pygame.draw.rect(self.screen, (255, 0, 0), [20,20,20,20], 3)

        #pygame.display.update(self.dude.rect)
        pygame.display.flip()


'''
Fonts: http://www.nerdparadise.com/tech/python/pygame/basics/part5/
'''
class GameText(object):

    def __init__(self):

        self.font_big = pygame.font.Font("assets/KOMIKAX_.ttf", 40) # Modus
        self.font_score = pygame.font.Font("assets/KOMIKAX_.ttf", 25) # Punkte
        self.font_time = pygame .font.Font("assets/KOMIKAX_.ttf", 25) # Zeit

    def get_score_text(self, score):
        score_text = self.font_score.render("Score: " + str(score), True, (255, 255, 255))
        return score_text

    def get_time(self, time):
        time_text = self.font_time.render("Time: " + str(time), True, (255, 255, 255))
        return time_text

    def get_announce_text1(self):
        return self.font_big.render("Party Hard!", True, (255, 0, 0))

    def get_announce_text2(self):
        return self.font_big.render("Study Time!", True, (0, 0, 255))
