'''
https://www.daniweb.com/software-development/python/code/468974/play-wave-sound-files-with-pygame
http://www.pygame.org/docs/ref/mixer.html
'''


#----------------------------------------------------------------------

import pygame

class GameSound(object):
    def __init__(self):
        self.sounds = []

    #----------------------------------------------------------------------

    def load_game_paused_track(self):
        sound = pygame.mixer.Sound("assets/dream.WAV")
        self.sounds.append(sound)
        return sound

    def load_party_track(self):
        sound = pygame.mixer.Sound("assets/rock2.WAV")
        self.sounds.append(sound)
        return sound

    def load_study_track(self):

    	sound = pygame.mixer.Sound("assets/rock.WAV")
        self.sounds.append(sound)
    	return sound

    def stop_all_sounds(self):
        for sound in self.sounds:
            sound.stop()