from Constants import *

class Config:
    @classmethod
    def readConfig(cls):
        fichier = open("./config/color.cfg", "r")
        config_color = fichier.read().splitlines()  # va lire le fichier,de couleur
        fichier.close()
        cfg_color = (int(config_color[0]), int(config_color[1]), int(config_color[2]))
        Constants.bg_color = cfg_color
        return cfg_color

    @classmethod
    def setConfig(cls, new_color):
        fichier = open("./config/color.cfg", "w")
        try:
            fichier.write(str(new_color[0]) + "\n")
            fichier.write(str(new_color[1]) + "\n")
            fichier.write(str(new_color[2]) + "\n")
        except:
            fichier.write("0\n")
            fichier.write("0\n")
            fichier.write("0\n")
        fichier.close()