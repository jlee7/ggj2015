from weakref import WeakKeyDictionary
from time import time

class EventManager(object):

    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):
        self.listeners[listener] = True

    def post(self, event):
        print "Event: " + event.name
        for listener in self.listeners:
            listener.notify(event)

    def test(self):
        print "Testausgabe"

class Event(object):
    def __init__(self):
        self.name = "Generic Event"

class TickEvent(Event):
    def __init__(self):
        self.name = "Timer Tick"
