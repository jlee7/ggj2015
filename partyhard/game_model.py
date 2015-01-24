from event_manager import *
from item_models import *
import random

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
            if(event.tick_number % 15 == 0):
                self.spawn_item()
        elif isinstance (event, CollisionEvent):
            if self.partytime:
                if event.item.partytime:
                    self.score += 5
                else:
                    self.score -= 5
            else:
                if event.item.partytime:
                    self.score -= 5
                else:
                    self.score += 5
        elif isinstance (event, PartyTimeSwitch):
            if self.partytime == True:
                self.partytime = False
            else:
                self.partytime = True
        elif isinstance(event, StopGameEvent):
            pass



    def spawn_item(self):
        item_model = random.choice([BeerModel(),CocktailModel(),BookModel(),PenModel()])
        self.event_manager.post(SpawnItemEvent(item_model))

        
