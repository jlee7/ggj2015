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

    def load_sound_mmmh(self):
        sound = pygame.mixer.Sound("assets/mmmh.wav")
        return sound

    def load_sound_no(self):
        sound = pygame.mixer.Sound("assets/no.wav")
        return sound

    def load_sound_no2(self):
        sound = pygame.mixer.Sound("assets/no2.wav")
        return sound

    def load_sound_partyhard(self):
        sound = pygame.mixer.Sound("assets/partyhard.wav")
        return sound

    def load_sound_partytime(self):
        sound = pygame.mixer.Sound("assets/partytime.wav")
        return sound

    def load_sound_studytime(self):
        sound = pygame.mixer.Sound("assets/studytime.wav")
        return sound

    def load_sound_whatdowedonow(self):
        sound = pygame.mixer.Sound("assets/whatdowedonow.wav")
        return sound

    def load_sound_yeah(self):
        sound = pygame.mixer.Sound("assets/yeah.wav")
        return sound