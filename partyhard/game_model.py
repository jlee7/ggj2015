from event_manager import *
from item_models import *
import random
import urllib
import hashlib
import socket

SALT = "JosefManu"
SCORE_POSITIV_CATCH = 10
SCORE_NEGATIVE_CATCH = 5

#----------------------------------------------------------------------

class GameModel(object):

    STATE_PREPARING = 'preparing'
    STATE_RUNNING = 'running'
    STATE_PAUSED = 'paused'

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.items = []
        self.score = 0
        self.partytime = True
        self.state = self.STATE_RUNNING
        #print urllib.urlopen("http://partyhard.p2-lab.com/submit.php?player=sdf&doof=3")
        #print hashlib.sha224("300"+SALT).hexdigest()

    #----------------------------------------------------------------------

    def notify(self, event):
        if isinstance (event, TickEvent):
            if(event.tick_number % random.randrange(3,15) == 0):
                self.spawn_item()
        elif isinstance (event, CollisionEvent):
            self.grant_score(event)
        elif isinstance (event, PartyTimeSwitch):
            self.flip_partytime()
        elif isinstance(event, StopGameEvent):
            self.state = self.STATE_PAUSED
            # hghscore
            hashed_score = hashlib.sha224(str(self.score)+SALT).hexdigest()
            hostname = socket.gethostname()
            url = "http://partyhard.p2-lab.com/submit.php?score=" + str(self.score) + "&hash=" + hashed_score + "&hname=" + hostname
            urllib.urlopen(url)
        elif isinstance(event, RestartGameEvent):
            self.restart_game()


    def restart_game(self):
        self.score = 0
        self.partytime = True
        self.state = self.STATE_RUNNING
        print "GameModel: restart game"
        
        

    def grant_score(self, event):
        if self.partytime:
            if event.item.partytime:
                self.score += SCORE_POSITIV_CATCH
                self.event_manager.post(ItemCatchPositive())
            else:
                self.score -= SCORE_NEGATIVE_CATCH
                self.event_manager.post(ItemCatchNegative())
        else:
            if event.item.partytime:
                self.score -= SCORE_NEGATIVE_CATCH
                self.event_manager.post(ItemCatchNegative())
            else:
                self.score += SCORE_POSITIV_CATCH
                self.event_manager.post(ItemCatchPositive())

    def flip_partytime(self):
        if self.partytime == True:
            self.partytime = False
        else:
            self.partytime = True

    def spawn_item(self):
        item_model = random.choice([BeerModel(self),CocktailModel(self),BookModel(self),PenModel(self)])
        #item_model = random.choice([BeerModel(self)])
        self.event_manager.post(SpawnItemEvent(item_model))

        
