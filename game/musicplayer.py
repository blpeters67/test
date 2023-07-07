import pygame
from decimal import Decimal

class MusicPlayer:
    
    def __init__(self):
        self.muted = False
        self.volume = Decimal(0.7)
        
        # start the music player for the bg music
        pygame.mixer.music.load("assets/audio/idle.wav")
        pygame.mixer.music.queue("assets/audio/just_like_that.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(self.volume)

    def update(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("assets/audio/idle.wav")
            pygame.mixer.music.queue("assets/audio/just_like_that.wav")
            pygame.mixer.music.play()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def increase_volume(self):
        if round(self.volume, 1) < 1:
            self.volume += Decimal(0.1)
        if not self.muted:
            self.set_volume(self.volume)

    def decrease_volume(self):
        if round(self.volume, 1) > 0:
            self.volume -= Decimal(0.1)
        if not self.muted:
            self.set_volume(self.volume)

    def mute(self):
        if not self.muted:
            self.muted = True
            pygame.mixer.music.set_volume(0)
        else:
            self.muted = False
            pygame.mixer.music.set_volume(self.volume)