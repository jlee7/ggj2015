from event_manager import *
from item_models import *
import random

SCORE_POSITIV_CATCH = 5
SCORE_NEGATIVE_CATCH = 10

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
        self.state = GameModel.STATE_PREPARING

    #----------------------------------------------------------------------

    def notify(self, event):
        if isinstance (event, TickEvent):
            if(event.tick_number % random.randrange(3,15) == 0):
                self.spawn_item()
        elif isinstance (event, CollisionEvent):
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
        elif isinstance (event, PartyTimeSwitch):
            if self.partytime == True:
                self.partytime = False
            else:
                self.partytime = True
            print "partytime: " + str(self.partytime)
        elif isinstance(event, StopGameEvent):
            pass



    def spawn_item(self):
        item_model = random.choice([BeerModel(self),CocktailModel(self),BookModel(self),PenModel(self)])
        #item_model = random.choice([BeerModel(self)])
        self.event_manager.post(SpawnItemEvent(item_model))

        
