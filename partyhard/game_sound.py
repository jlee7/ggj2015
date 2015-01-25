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
        sound.set_volume(0.7)
        return sound

    def load_party_track(self):
        sound = pygame.mixer.Sound("assets/rock2.WAV")
        self.sounds.append(sound)
        sound.set_volume(0.7)
        return sound

    def load_study_track(self):
    	sound = pygame.mixer.Sound("assets/rock.WAV")
        self.sounds.append(sound)
        sound.set_volume(0.7)
        return sound


    def load_sound_mmmh(self):
        sound = pygame.mixer.Sound("assets/mmmh.wav")
        sound.set_volume(0.5)
        self.sounds.append(sound)

        return sound

    def load_sound_no(self):
        sound = pygame.mixer.Sound("assets/no.wav")
        sound.set_volume(0.3)
        self.sounds.append(sound)
        return sound

    def load_sound_no2(self):
        sound = pygame.mixer.Sound("assets/no2.wav")
        sound.set_volume(0.3)
        self.sounds.append(sound)
        return sound

    def load_sound_partyhard(self):
        sound = pygame.mixer.Sound("assets/partyhard.wav")
        sound.set_volume(0.9)
        self.sounds.append(sound)
        return sound

    def load_sound_partytime(self):
        sound = pygame.mixer.Sound("assets/partytime.wav")
        sound.set_volume(0.9)
        self.sounds.append(sound)
        return sound

    def load_sound_studytime(self):
        sound = pygame.mixer.Sound("assets/studytime.wav")
        sound.set_volume(0.9)
        self.sounds.append(sound)
        return sound

    def load_sound_whatdowedonow(self):
        sound = pygame.mixer.Sound("assets/whatdowedonow.wav")
        sound.set_volume(0.9)
        self.sounds.append(sound)
        return sound

    def load_sound_yeah(self):
        sound = pygame.mixer.Sound("assets/yeah.wav")
        sound.set_volume(0.4)
        self.sounds.append(sound)
        return sound

    def stop_all_sounds(self):
        for sound in self.sounds:
            sound.stop()

