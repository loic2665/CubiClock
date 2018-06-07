import pygame
pygame.mixer.init()

print("Mixer Audio OK")

bat_low = pygame.mixer.Sound("./sound/bat_low.wav")
alarm_ring = pygame.mixer.Sound("./sound/alarm/ring.wav")

startup = pygame.mixer.Sound("./sound/startup.wav")

print("File audio OK")

class Sound:
    @classmethod
    def jouerSon(cls, audio):
        audio.play()

    @classmethod
    def jouerSonLoop(cls, audio):
        audio.play(-1)

    @classmethod
    def stopSon(cls, audio):
        audio.stop()