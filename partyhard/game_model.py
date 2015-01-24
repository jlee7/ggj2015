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
        self.item_types = ['beer','cocktail','book','pen']

    #----------------------------------------------------------------------

    def notify(self, event):
        # logic: alle n ticks eine object spawnen

        if isinstance (event, TickEvent):
            if(event.tick_number % 15 == 0):
                #print event.tick_number
                self.spawn_item(random.choice(self.item_types))

    def spawn_item(self, item_type):

        if item_type == 'beer':
            item_model = BeerModel()
        elif item_type == 'cocktail':
            item_model = CocktailModel()         
        elif item_type == 'book':
            item_model = BookModel()         
        elif item_type == 'pen':
            item_model = PenModel()  

        item_model = random.choice([BeerModel(),CocktailModel(),BookModel(),PenModel()])

        self.event_manager.post(SpawnItemEvent(item_model))

        #self.items.append(item)
        #print "Itemsanzahl: " + str(len(self.items))
