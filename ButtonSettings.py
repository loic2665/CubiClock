import pygame

from Constants import *
from Ecran import *
from Config import *

long = 48
larg = 48
x = 20
y = 180

class Back:
    def __init__(self):
        self.rect = pygame.Rect(10, 45, 48, 53)

    def show(self):
        Ecran.drawImage(back, (10, 45))

    def onMouseClick(self):
        print("Back")
        Constants.screen = "clock"

class Blue:
    def __init__(self):
        self.rect = pygame.Rect((x+1*(long+10), y, long, larg))

    def show(self):
        Ecran.drawRectangle((x+1*(long+10), y), (long, larg), blue)


    def onMouseClick(self):
        print("Blue")
        Config.setConfig(blue)
        Constants.screen = "clock"


class Red:
    def __init__(self):
        self.rect = pygame.Rect((x+2*(long+10), y, long, larg))

    def show(self):
        Ecran.drawRectangle((x+2*(long+10), y), (long, larg), red)

    def onMouseClick(self):
        print("Red")
        Config.setConfig(red)
        Constants.screen = "clock"


class Green:
    def __init__(self):
        self.rect = pygame.Rect((x+3*(long+10), y, long, larg))

    def show(self):
        Ecran.drawRectangle((x+3*(long+10), y), (long, larg), green)

    def onMouseClick(self):
        print("Green")
        Config.setConfig(green)
        Constants.screen = "clock"


class Orange:
    def __init__(self):
        self.rect = pygame.Rect((x+4*(long+10), y, long, larg))

    def show(self):
        Ecran.drawRectangle((x+4*(long+10), y), (long, larg), orange)

    def onMouseClick(self):
        print("Orange")
        Config.setConfig(orange)
        Constants.screen = "clock"


class Pink:
    def __init__(self):
        self.rect = pygame.Rect((x+5*(long+10), y, long, larg))

    def show(self):
        Ecran.drawRectangle((x+5*(long+10), y), (long, larg), pink)

    def onMouseClick(self):
        print("Pink")
        Config.setConfig(pink)
        Constants.screen = "clock"


class Black:
    def __init__(self):
        self.rect = pygame.Rect((x+6*(long+10), y, long, larg))

    def show(self):
        Ecran.drawRectangle((x+6*(long+10), y), (long, larg), black)

    def onMouseClick(self):
        print("Black")
        Config.setConfig(black)
        Constants.screen = "clock"

