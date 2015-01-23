from event_manager import *
import pygame

tick_speed = 15 # framerate

clock = pygame.time.Clock()

class TimeController(object):

    def __init__(self, event_manager):
        self.tick = 0
        self.event_manager = event_manager
        self.event_manager.register_listener(self)

    def run(self):
        while True:
            clock.tick(tick_speed)
            self.tick += 1
            print "Tick: " + str(self.tick)
            event = TickEvent()
            self.event_manager.post(event)

    def notify(self, event):
        pass
