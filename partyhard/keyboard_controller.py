from event_manager import *
import pygame


class KeyboardController(object):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.register_listener(self)
        self.keys = [False, False]


    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_a:
                        self.keys[0]=True
                    elif event.key==pygame.K_d:
                        self.keys[1]=True

                if event.type == pygame.KEYUP:
                    if event.key==pygame.K_a:
                        self.keys[0]=False
                    elif event.key==pygame.K_d:
                        self.keys[1]=False
            direction = False
            if self.keys[0]:
                direction = "left"
            elif self.keys[1]:
                direction = "right"
            if direction:
            	self.evManager.post(DudeMoveEvent(direction))