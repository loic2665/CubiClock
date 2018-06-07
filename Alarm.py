from Constants import *

class Alarm:
    @classmethod
    def readAlarm(cls):
        config_alarm = ['', '', '']
        fichier = open("./config/alarm.cfg", "r")
        config_alarm = fichier.read().splitlines()  # va lire le fichier, puis, chaques ligne va le mettre dans un element du tableau ['H','M','on/off']
        fichier.close()
        i_heure = config_alarm[0]
        i_min = config_alarm[1]
        if config_alarm[-1] == "on":
            Constants.alarm = [True, i_heure, i_min]
        else:
            Constants.alarm =  [False, i_heure, i_min]




    @classmethod
    def writeAlarm(cls, active, h, m):
        fichier = open("./config/alarm.cfg", "w")
        fichier.write("{}\n".format(h))
        fichier.write("{}\n".format(m))
        if active:
            fichier.write("on\n")
        else:
            fichier.write("off\n")
        fichier.close()
        Constants.screen = "clock"
        Constants.alarmStopped = False



