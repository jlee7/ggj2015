from event_manager import *
from item_models import *


#----------------------------------------------------------------------

class GameModel(object):

    def __init__(self, event_manager):

        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.items = []

    #----------------------------------------------------------------------

    def notify(self, event):
        # logic: alle n ticks eine object spawnen

        if isinstance (event, TickEvent):
            if(event.tick_number % 15 == 0):
                print event.tick_number
                self.spawn_item()

    def spawn_item(self):
        item = BeerModel()
        spawn_event = SpawnItemEvent(item)
        self.event_manager.post(spawn_event)
        #self.items.append(item)
        #print "Itemsanzahl: " + str(len(self.items))
