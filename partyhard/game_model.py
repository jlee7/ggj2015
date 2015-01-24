from event_manager import *
from item_models import *
import random

#----------------------------------------------------------------------

class GameModel(object):

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.items = []
        self.score = 0

    #----------------------------------------------------------------------

    def notify(self, event):
        if isinstance (event, TickEvent):
            if(event.tick_number % 15 == 0):
                self.spawn_item()
        elif isinstance (event, CollisionEvent):
            

    def spawn_item(self):  
        item_model = random.choice([BeerModel(),CocktailModel(),BookModel(),PenModel()])
        self.event_manager.post(SpawnItemEvent(item_model))

