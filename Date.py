from time import *

class Date:
    @classmethod
    def getDate(cls):
        strings = strftime("%Y,%m,%d,%H,%M,%S")  # mise de la date dd/mm/yyyy
        t = strings.split(',')
        date = [str(x) for x in t]
        return date