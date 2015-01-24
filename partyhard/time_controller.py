from event_manager import *
import pygame

tick_speed = 30 # framerate

clock = pygame.time.Clock()

#----------------------------------------------------------------------

class TimeController(object):

    def __init__(self, event_manager):
        self.tick_number = 0
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    #----------------------------------------------------------------------

    def run(self):
        while True:
            clock.tick(tick_speed)
            self.tick_number += 1
            #print "Tick: " + str(self.tick_number)
            event = TickEvent(self.tick_number)
            self.event_manager.post(event)

    #----------------------------------------------------------------------
    
    def notify(self, event):
        pass
