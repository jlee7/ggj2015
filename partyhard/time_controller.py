from event_manager import *
import pygame
import random

GAME_LENGTH_SEC = 10
GAME_LENGTH = GAME_LENGTH_SEC * 1000
tick_speed = 30 # framerate

clock = pygame.time.Clock()

#----------------------------------------------------------------------

class TimeController(object):

    def __init__(self, event_manager):
        self.tick_number = 0
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.game_time = 0.0
        self.keep_running = True
        self.next_switch_tick = self.get_next_switch_delay()

    #----------------------------------------------------------------------

    def run(self):
        while True:

            clock.tick(tick_speed)

            # End Game Event
            if self.game_time > GAME_LENGTH:
                #self.event_manager.post(StopGameEvent())
                pass

            # Switch game modes 
            if self.tick_number == self.next_switch_tick:
               self.party_time_switch()

            # Tick Event
            self.tick_number += 1
            self.game_time += clock.get_time() 
            event = TickEvent(self.tick_number, self.game_time)
            self.event_manager.post(event)

    #----------------------------------------------------------------------
    
    def get_next_switch_delay(self):
        return random.randrange(200, 300)

    def party_time_switch(self):
        self.event_manager.post(PartyTimeSwitch())
        self.next_switch_tick = self.tick_number + self.get_next_switch_delay()

    def get_countdown_time(self):
        return (GAME_LENGTH_SEC - (self.game_time / 1000))

    def notify(self, event):
        pass
