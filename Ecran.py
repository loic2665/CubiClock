import pygame


batt_4 = pygame.image.load("./icon/battery/battery-4.png")
batt_3 = pygame.image.load("./icon/battery/battery-3.png")
batt_2 = pygame.image.load("./icon/battery/battery-2.png")
batt_1 = pygame.image.load("./icon/battery/battery-1.png")
batt_0 = pygame.image.load("./icon/battery/battery-0.png")
batt_empty = pygame.image.load("./icon/battery/battery-empty.png")

print("Batt icons OK")

alarm = pygame.image.load("./icon/alarm/alarm.png")
alarm_on = pygame.image.load("./icon/alarm/on.png")
alarm_off = pygame.image.load("./icon/alarm/off.png")
alarm_ok = pygame.image.load("./icon/alarm/ok.png")
alarm_stop = pygame.image.load("./icon/alarm/stop.png")

cadre = pygame.image.load("./icon/alarm/cadre.png")
hPlus = pygame.image.load("./icon/alarm/fleche_plus.png")
hMoins = pygame.image.load("./icon/alarm/fleche_moins.png")

print("Alarm icons OK")

calendar = pygame.image.load("./icon/calendar/calendar.png")


config = pygame.image.load("./icon/config/config.png")

print("Config icons OK")

weather_cloudy = pygame.image.load("./icon/weather/cloudy.png")
weather_loading = pygame.image.load("./icon/weather/loading.png")
weather_rain = pygame.image.load("./icon/weather/rain.png")
weather_sun = pygame.image.load("./icon/weather/sun.png")

print("Weather icons OK")

btc_20 = pygame.image.load("./icon/btc/btc-20.png")
btc_72 = pygame.image.load("./icon/btc/btc-72.png")

print("Bitcoin icons OK")

back = pygame.image.load("./icon/utils/back.png")

print("Utils icons OK")


print("Image OK")

#couleur
red = (187,0,0)
green = (0,255,0)
blue = (0,0,255)
lightblue = (42,134,198)
white = (255,255,255)
black = (0,0,0)
pink = (224,17,95) #SET|48|0|255
orange = (255,165,0)


print("Color OK")


pygame.init()
FPSCLOCK = pygame.time.Clock()
pygame.mixer.init()
# Ouverture de la fenêtre Pygame
taille_fen_x = 480
taille_fen_y = 320
fenetre = pygame.display.set_mode((taille_fen_x, taille_fen_y))
#pygame.display.toggle_fullscreen()


class Ecran:
    @classmethod
    def updateScreen(cls):
        FPSCLOCK.tick(60)
        pygame.display.update()

    @classmethod
    def afficher_texte(cls, msg, dim, pos, color):
        fontObj = pygame.font.Font('./font/Arial_Bold.ttf', int(dim))
        textSurfaceObj = fontObj.render(msg, True, color)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft = pos
        fenetre.blit(textSurfaceObj, textRectObj)
        pygame.display.update(textRectObj)

    @classmethod
    def drawRectangle(cls, pos, taille, color):
        dim = pygame.Rect(pos[0], pos[1], taille[0], taille[1])
        pygame.draw.rect(fenetre, color, dim)

    @classmethod
    def drawImage(cls, img, pos):
        fenetre.blit(img, pos)

    @classmethod
    def recouvrir(cls, color):
        fenetre.fill(color)
