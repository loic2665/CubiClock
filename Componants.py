from Date import *
from Ecran import *
from Constants import *
from Sound import *
class Componant:
    @classmethod
    def drawHUD(cls):

        Ecran.drawRectangle((10, 32), (460, 2), Constants.bg_color)  # barre horizontale

        # barre 1

        pygame.draw.rect(fenetre, white, pygame.Rect(134, 8, 2, 18))  # barre 1
        Ecran.drawRectangle((134,8), (2, 18), white)  # barre 1

        Ecran.drawImage(calendar, (12, 7))

        date = Date.getDate()

        Ecran.afficher_texte(date[2] + "/" + date[1] + "/" + date[0], 18, (38, 9), white)

        # barre 2

        Ecran.drawRectangle((253,8), (2, 18), white)  # barre 1

        Ecran.drawImage(btc_20, (139, 8))

        # bitcoin prix dans HUD


        if Constants.bitcoinPrice == "wait":
            Ecran.afficher_texte(Constants.bitcoinPrice, 18, (165, 8), white)
        else:
            Ecran.afficher_texte(str(Constants.bitcoinPrice) + " €", 18, (165, 8), white)

        # barre 3

        alarm_x = 259
        alarm_y = 8

        Ecran.drawImage(alarm, (259, 8))
        if Constants.alarm[0]:

            Ecran.afficher_texte("{:>02} : {:>02}".format(Constants.alarm[1], Constants.alarm[2]), 18, (alarm_x + 25, alarm_y), white)
        else:
            Ecran.afficher_texte("Non", 15, (alarm_x + 30, alarm_y + 2), white)

        Ecran.drawRectangle((349, 8), (2, 18), white)
        # barre 4

        Ecran.drawImage(config, (359, 8))

        # barre 5

        Ecran.drawRectangle((385, 8), (2, 18), white)  # barre 4

        battery_x = 394
        battery_y = 7

        if Constants.voltageBattery <= 5.0 and Constants.voltageBattery > 3.9:
            fenetre.blit(batt_4, (battery_x, battery_y))
        if Constants.voltageBattery <= 3.9 and Constants.voltageBattery > 3.7:
            fenetre.blit(batt_3, (battery_x, battery_y))
        if Constants.voltageBattery <= 3.7 and Constants.voltageBattery > 3.65:
            fenetre.blit(batt_2, (battery_x, battery_y))
        if Constants.voltageBattery <= 3.65 and Constants.voltageBattery > 3.6:
            fenetre.blit(batt_1, (battery_x, battery_y))
        if Constants.voltageBattery <= 3.6:
            fenetre.blit(batt_0, (battery_x, battery_y))

        if Constants.voltageBattery <= 3.65:

            if Constants.timer_batt_sound > 50:  # on previent la batterie faible apres 10 secondes
                Constants.timer_batt_sound = 0
                Sound.jouerSon(bat_low)
            else:
                Constants.timer_batt_sound += 1

            if Constants.timer_batt_sound < 3:  # ON FAIT CLIGNOTER LA BATTERIE MAIS EN FAIT JE MET UN PUTAIN DE RECTANGLE BLEU MDR
                Ecran.drawRectangle((battery_x, battery_y), (72, 20),Constants.bg_color)  # latille de l'image de la batterie est de 72*20
                Constants.timer_batt_sound += 1
            else:
                if Constants.timer_batt_sound >= 3 and Constants.timer_batt_sound < 6:
                    if Constants.voltageBattery <= 3.65 and Constants.voltageBattery > 3.6:
                        fenetre.blit(batt_1, (battery_x, battery_y))
                    if Constants.voltageBattery <= 3.6:
                        fenetre.blit(batt_0, (battery_x, battery_y))
                        Constants.voltageBattery += 1
                else:
                    Constants.timer_batt_blink = 0
