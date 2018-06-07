import pygame

from Constants import *
from Sound import *



class Settings:
    def __init__(self):
        self.rect = pygame.Rect(359, 8, 20, 20)

    def onMouseClick(self):
        print("Settings")
        Constants.screen = "settings"

class Battery:
    def __init__(self):
        self.rect = pygame.Rect(393, 8, 72, 20)

    def onMouseClick(self):
        print("Battery")
        Constants.screen = "battery"

class AlarmSettings:
    def __init__(self):
        self.rect = pygame.Rect(259, 8, 87, 20)

    def onMouseClick(self):
        print("AlarmSettings")
        Constants.screen = "alarm"
