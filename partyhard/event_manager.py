from weakref import WeakKeyDictionary
from time import time


#----------------------------------------------------------------------

class EventManager(object):

    def __init__(self):
        self.listeners = WeakKeyDictionary()
        self.last_tick = 0

    #----------------------------------------------------------------------

    def register_listener(self, listener):
        self.listeners[listener] = True

    #----------------------------------------------------------------------

    def post(self, event):
        if not isinstance (event, TickEvent):
            print "Event: " + event.name + " (" + str(self.last_tick) + ")"
        else:
            self.last_tick = event.tick_number

        for listener in self.listeners:
            #print event
            listener.notify(event)

    #----------------------------------------------------------------------

    def test(self):
        print "Testausgabe"

#----------------------------------------------------------------------

class Event(object):
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self, tick_number):
        self.name = "Timer Tick"
        self.tick_number = tick_number

class DudeMoveEvent(Event):
    def __init__(self, direction):
        self.name = "Dude Move"
        self.direction = direction

class SpawnItemEvent(Event):
    def __init__(self, item):
        self.item = item
        self.name = "Spawn Item"

