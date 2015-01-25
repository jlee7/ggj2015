from event_manager import *
from item_models import *
import random

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
        elif isinstance(event, RestartGameEvent):
            self.restart_game()

    def restart_game(self):
        self.score = 0
        self.partytime = True
        self.state = self.STATE_RUNNING

    def grant_score(self, event):
        if self.partytime:
            if event.item.partytime:
                self.score += SCORE_POSITIV_CATCH
            else:
                self.score -= SCORE_NEGATIVE_CATCH
        else:
            if event.item.partytime:
                self.score -= SCORE_NEGATIVE_CATCH
            else:
                self.score += SCORE_POSITIV_CATCH

    def flip_partytime(self):
        if self.partytime == True:
            self.partytime = False
        else:
            self.partytime = True

    def spawn_item(self):
        item_model = random.choice([BeerModel(self),CocktailModel(self),BookModel(self),PenModel(self)])
        #item_model = random.choice([BeerModel(self)])
        self.event_manager.post(SpawnItemEvent(item_model))

        
