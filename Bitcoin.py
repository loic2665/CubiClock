import urllib
import json

from Constants import *

class Bitcoin:
    @classmethod
    def getBitcoinPrice(cls):
        try:
            request = urllib.request.urlopen('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR', timeout=2)
            status = request.read().decode()  # decode "request" (binaire) en str
            bitcoin = json.loads(status)
            Constants.bitcoinPrice = bitcoin["EUR"]
        except:
            Constants.bitcoinPrice = "err"

