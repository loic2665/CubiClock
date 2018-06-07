from Constants import *
import urllib.request
import json

class Weather:
    @classmethod
    def getWeather(cls):
        try:
            print("Weather")
            request = urllib.request.urlopen('http://openweathermap.org/data/2.5/weather?q=Liege,be&appid=b6907d289e10d714a6e88b30761fae22',timeout=2)
            status = request.read().decode()  # decode "request" (binaire) en str
            print(status)
            weather = json.loads(status)

            weather_main = weather["weather"][0]["main"] + "|"
            weather_description = weather["weather"][0]["description"] + "|"
            weather_temp = str(int(weather["main"]["temp"])) + "|"
            weather_wind = str(int(weather["wind"]["speed"]))

            Constants.weather = "ok|" + weather_main + weather_description + weather_temp + weather_wind
            print(Constants.weather)

        except:
            Constants.weather = "err||||"  # status|nom|description|temp|vent

