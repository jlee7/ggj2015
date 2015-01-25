from event_manager import *
import pygame

#----------------------------------------------------------------------
class KeyboardController(object):

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.register_listener(self)
        self.keys = [False, False]
        self.controlkeys =[False]

    #----------------------------------------------------------------------

    def notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                self.quit_if_we_must(event)
                self.collect_user_game_inputs(event)
            self.process_user_game_inputs()

    #----------------------------------------------------------------------

    def quit_if_we_must(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:
                self.evManager.post(RestartGameEvent())

    #----------------------------------------------------------------------

    def collect_user_game_inputs(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_a:
                self.keys[0]=True
            elif event.key==pygame.K_d:
                self.keys[1]=True
            elif event.key ==pygame.K_m:
                self.controlkeys[0]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_a:
                self.keys[0]=False
            elif event.key==pygame.K_d:
                self.keys[1]=False
            elif event.key==pygame.K_m:
                self.controlkeys[0]=False

    #----------------------------------------------------------------------

    def process_user_game_inputs(self):
        direction = False
        if self.keys[0]:
            direction = "left"
        elif self.keys[1]:
            direction = "right"
        if direction:
            self.evManager.post(DudeMoveEvent(direction))
        if self.controlkeys[0]:
            self.evManager.post(PartyTimeSwitch())