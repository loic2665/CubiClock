import pygame

from Alarm import *
from Constants import *
from Sound import *
from Ecran import *

class AlarmSettingsOk:
    def __init__(self):
        self.rect = pygame.Rect(340, 250, 100, 45)

    def show(self):
        Ecran.drawImage(alarm_ok, (340, 250))

    def onMouseClick(self):
        print("alarmConfirm")
        Alarm.writeAlarm(Constants.alarmTemp[0],Constants.alarmTemp[1],Constants.alarmTemp[2])
        Constants.timer_alarm = 31


class AlarmSwitch:
    def __init__(self):
        self.rect = pygame.Rect(363, 173, 48, 48)

    def show(self):
        if Constants.alarmTemp[0]:
            Ecran.drawImage(alarm_on, (363, 173))
        else:
            Ecran.drawImage(alarm_off, (363, 173))

    def onMouseClick(self):
        print("alarmSwitch")
        if Constants.alarmTemp[0]:
            Constants.alarmTemp[0] = False
        else:
            Constants.alarmTemp[0] = True



class heurePlus:
    def __init__(self):
        self.rect = pygame.Rect(100, 125, 96, 48)

    def show(self):
        Ecran.drawImage(hPlus, (100, 125))

    def onMouseClick(self):
        Constants.alarmTemp[1] += 1
        print("heurePlus")


class heureMoins:
    def __init__(self):
        self.rect = pygame.Rect(100, 240, 96, 48)

    def show(self):
        Ecran.drawImage(hMoins, (100, 240))

    def onMouseClick(self):
        Constants.alarmTemp[1] -= 1
        print("heureMoins")


class minPlus:
    def __init__(self):
        self.rect = pygame.Rect(200, 125, 96, 48)

    def show(self):
        Ecran.drawImage(hPlus, (200, 125))

    def onMouseClick(self):
        Constants.alarmTemp[2] += 1
        print("minPlus")

class minMoins:
    def __init__(self):
        self.rect = pygame.Rect(200, 240, 96, 48)

    def show(self):
        Ecran.drawImage(hMoins, (200, 240))

    def onMouseClick(self):
        Constants.alarmTemp[2] -= 1
        print("minMoins")

class checkData:
    @classmethod
    def check(cls):

        if Constants.alarmTemp[1] > 23:
            Constants.alarmTemp[1] = 0
        if Constants.alarmTemp[1] < 0:
            Constants.alarmTemp[1] = 23

        if Constants.alarmTemp[2] > 59:
            Constants.alarmTemp[2] = 0
            Constants.alarmTemp[1] += 1
        if Constants.alarmTemp[2] < 0:
            Constants.alarmTemp[2] = 59
            Constants.alarmTemp[1] -= 1

######################################################
################# POUR ALARM RING ####################
######################################################


class AlarmStop:
    def __init__(self):
        self.rect = pygame.Rect(191, 212, 100, 45)

    def show(self):
        Ecran.drawImage(alarm_stop, (10, 45))

    def onMouseClick(self):
        print("Back")
        Constants.screen = "clock"
        Sound.stopSon(alarm_ring)
