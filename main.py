# -*- coding:utf-8 -*-


print("Script lancé !")

import pygame
from pygame.locals import *

print("Pygame OK")

import sys
import datetime
import os
from time import *
import json
import random
import serial
# import RPi.GPIO as GPIO
import threading

from Constants import *
from Componants import *
from Ecran import *
from Alarm import *
from Config import *
from Date import *
from Weather import *
from Bitcoin import *
from Sensors import *
from LEDs import *
from ButtonClock import *
from ButtonSettings import *
from ButtonAlarm import *
print("Prerequi OK")

# coordonnée de la souris
cursor_x = 0
cursor_y = 0

print("File audio OK")

arret = False

Constants.bg_color = Config.readConfig()

#Sound.jouerSon(startup)

clockMenu = [Settings(), Battery(), AlarmSettings()]
settingsMenu = [Back(), Blue(), Red(), Green(), Orange(), Pink(), Black()]
alarmRing = [AlarmStop()]
alarmSettings = [Back(), heureMoins(), heurePlus(), minMoins(), minPlus(), AlarmSettingsOk(), AlarmSwitch()]
batteryMenu = [Back()]

while True:
    Ecran.recouvrir(Constants.bg_color)
    Componant.drawHUD()

    #################################################################################################################
    #################################################################################################################
    ###################################### TIMER ############# NE PAS ENLEVER #######################################
    ################################################## svp ##########################################################
    #################################################################################################################


    if Constants.timer_weather > 30:  # on execute la fonction toute les 300 frames (300/30 fps) = 10 secondes (si sur l'ecran d'acceuil)
        threading.Timer(0, Weather.getWeather).start()
        Constants.timer_weather = 0
    else:
        Constants.timer_weather += 1

    if Constants.timer_bitcoin > 30:  # on execute la fonction toute les 300 frames (300/30 fps) = 10 secondes (si sur l'ecran d'acceuil)
        threading.Timer(0, Bitcoin.getBitcoinPrice).start()
        Constants.timer_bitcoin = 0
    else:
        Constants.timer_bitcoin += 1

    if Constants.timer_sensors > 30:  # on execute la fonction toute les 300 frames (300/30 fps) = 10 secondes (si sur l'ecran d'acceuil)
        threading.Timer(0, Sensors.getSensorsValue).start()
        Constants.timer_sensors = 0
    else:
        Constants.timer_sensors += 1

    if Constants.timer_alarm > 30:  # on execute la fonction toute les 300 frames (300/30 fps) = 10 secondes (si sur l'ecran d'acceuil)
        threading.Timer(0, Alarm.readAlarm).start()
        Constants.timer_alarm = 0
    else:
        Constants.timer_alarm += 1

    if Constants.timer_config > 30:  # on execute la fonction toute les 300 frames (300/30 fps) = 10 secondes (si sur l'ecran d'acceuil)
        threading.Timer(0, Config.readConfig).start()
        Constants.timer_config = 0
    else:
        Constants.timer_config += 1

    if Constants.timer_led > 30:  # on execute la fonction toute les 300 frames (300/30 fps) = 10 secondes (si sur l'ecran d'acceuil)
        threading.Timer(0, LEDs.setLEDs).start()
        Constants.timer_led = 0
    else:
        Constants.timer_led += 1


    #################################################################################################################
    #################################################################################################################
    ###################################### FIN TIMER ######### NE PAS ENLEVER #######################################
    ################################################## svp ##########################################################
    #################################################################################################################

    if Constants.screen == "clock":

        date = Date.getDate()
        heure = str(date[3] + ":" + date[4])

        Ecran.afficher_texte(heure, 112, (20, 60), white)
        try:
            temp = float(Constants.sensors_data[1])
            temp = int(temp - 3)
            temp = str(temp)

            Ecran.afficher_texte("T° / Hum :", 24, (326, 45), white)
            Ecran.afficher_texte("{}°C".format(temp), 52, (326, 70), white)

            hum = float(Constants.sensors_data[2])
            hum = int(hum)
            hum = str(hum)

            Ecran.afficher_texte("{}%".format(hum), 52, (326, 120), white)
        # afficher_texte(sec, 64, (sec_x, sec_y), white)
        except:
            Ecran.afficher_texte("T° / Hum :", 24, (326, 45), white)
            Ecran.afficher_texte("--°C", 52, (326, 70), white)
            Ecran.afficher_texte("--%", 52, (326, 120), white)

        ###### VERIF HEURE #######
        if date[3] == str(Constants.alarm[1]) and date[4] == str(Constants.alarm[2]) and Constants.alarm[0] == True and Constants.alarmStopped == False:
            Constants.screen = "wakeup"
            Constants.alarmStopped = True
            Sound.jouerSonLoop(alarm_ring)
        ###### FIN VERIF H #######

        ##### REINITIALISATION DE l4HORLOGE A MINUIT ######
        if date[3] == "00" and date[4] == "00":
            Constants.alarmStopped = False

        ######## METEO DEBUT #########

        weather_x = 35  # emplacement de l'icone
        weather_y = 200

        weather_text_x = 157  # emplacement du texte a droite de l'icone
        weather_text_y = 230

        weather_degres_x = 300  # emplacement du texte pour la temperature
        weather_degres_y = 210

        weather_wind_x = 300  # emplacement du texte pour la temperature
        weather_wind_y = 255

        weatherStatus_list = Constants.weather.split("|")
        if (weatherStatus_list[0] == "wait"):

            Ecran.afficher_texte("En attente...", 28, (weather_text_x, weather_text_y), white)
            Ecran.drawImage(weather_loading, (weather_x, weather_y))

        elif (weatherStatus_list[0] == "err"):
            Ecran.afficher_texte("Pas de connexion internet...", 28, (50, 210), white)



        else:

            if weatherStatus_list[1] == "Rain":
                Ecran.afficher_texte("Pluie", 42, (weather_text_x, weather_text_y), white)
                Ecran.drawImage(weather_rain, (weather_x, weather_y))

            if weatherStatus_list[1] in ["Clouds","Mist"]:
                Ecran.afficher_texte("Nuageux", 30, (weather_text_x, weather_text_y), white)
                Ecran.drawImage(weather_cloudy, (weather_x, weather_y))

            if weatherStatus_list[1] in ["Clear"]:
                Ecran.afficher_texte("Clair", 42, (weather_text_x, weather_text_y), white)
                Ecran.drawImage(weather_sun, (weather_x, weather_y))

            Ecran.afficher_texte(weatherStatus_list[3] + "°C", 48, (weather_degres_x, weather_degres_y), white)
            Ecran.afficher_texte(weatherStatus_list[4] + " km/h", 48, (weather_wind_x, weather_wind_y), white)

    if Constants.screen == "alarm":


        for element in alarmSettings:
            element.show()
            checkData.check()

        title_x = 127
        title_y = 58


        Ecran.afficher_texte("Off / On", 20, (353, 137), white)
        Ecran.afficher_texte("Configurer l'alarme", 24, (title_x, title_y), white)


        Ecran.afficher_texte(str("{:02}".format(Constants.alarmTemp[1])) + ":" + str("{:02}".format(Constants.alarmTemp[2])), 72, (106, 165), white)



    if Constants.screen == "battery":
        back_x = 10
        back_y = 45

        title_x = 127
        title_y = 58

        Ecran.drawImage(back, (back_x, back_y))
        Ecran.afficher_texte("Info. batterie", 48, (title_x, title_y), white)
        Ecran.afficher_texte("Voltage : ", 24, (101, 161), white)
        Ecran.afficher_texte(str(round(Constants.voltageBattery, 3)) + " Volts", 18, (212, 165), white)

    if Constants.screen == "wakeup":
        Ecran.drawImage(cadre, (45, 51))
        Ecran.afficher_texte("Il est l'heure !", 50, (89, 95), white)
        date = Date.getDate()
        Ecran.afficher_texte(date[3] + ":" + date[4] + ":" + date[5], 40, (155, 156), white)
        Ecran.drawImage(alarm_stop, (191, 212))


    if Constants.screen == "settings":
        Ecran.afficher_texte("Configuration", 24, (127, 58), white)
        Ecran.afficher_texte("Couleur Fond/LED", 18, (25, 122), white)

        for element in settingsMenu:
            element.show()



    for event in pygame.event.get():  # Attente des événements

        if arret:
            pygame.quit()
            exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x = event.pos[0]
            y = event.pos[1]
            print(x, y)

            if x > 7 and y > 4 and x < 35 and y < 27:  # système pour arreter le programme si en plein ecran
                Constants.clickStop += 1
                if Constants.clickStop > 5:
                    arret = True

        if Constants.screen == "clock":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for objet in clockMenu:
                    if objet.rect.collidepoint(event.pos):
                        objet.onMouseClick()
                        break

        if Constants.screen == "settings":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for objet in settingsMenu:
                    if objet.rect.collidepoint(event.pos):
                        objet.onMouseClick()
                        break

        if Constants.screen == "wakeup":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for objet in alarmRing:
                    if objet.rect.collidepoint(event.pos):
                        objet.onMouseClick()
                        break

        if Constants.screen == "alarm":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for objet in alarmSettings:
                    if objet.rect.collidepoint(event.pos):
                        objet.onMouseClick()
                        break

        if Constants.screen == "battery":
            if event.type == pygame.MOUSEBUTTONDOWN:
                for objet in batteryMenu:
                    if objet.rect.collidepoint(event.pos):
                        objet.onMouseClick()
                        break
    FPSCLOCK.tick(8)
    Ecran.updateScreen()
