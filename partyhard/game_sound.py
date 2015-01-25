'''
https://www.daniweb.com/software-development/python/code/468974/play-wave-sound-files-with-pygame
http://www.pygame.org/docs/ref/mixer.html
'''


#----------------------------------------------------------------------

import pygame

class GameSound(object):
    def __init__(self):
        pass

    #----------------------------------------------------------------------

    def load_party_track(self):
        sound = pygame.mixer.Sound("assets/rock2.WAV")
        return sound

    def load_study_track(self):
        #sound = pygame.mixer.Sound("assets/dream.WAV")
    	sound = pygame.mixer.Sound("assets/rock.WAV")
    	return sound