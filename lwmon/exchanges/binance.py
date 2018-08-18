import requests
from .exchange import Exchange, TradePair


class BinanceExchange(Exchange):
    def __init__(self):
        super(BinanceExchange, self).__init__("Binance", "https://www.binance.com/api")
        pass

    def update(self):
        response = requests.get("{0}/v3/ticker/price".format(self.endpoint))
        if not response.ok:
            print("Unable to update data for {0}".format(self.name))
            return
        pass

    def update_tradepair(self, tradepair: TradePair):
        symbol = tradepair.coin1 + tradepair.coin2
        response = requests.get("{0}/v3/ticker/price?symbol={1}".format(self.endpoint, symbol))
        if not response.ok:
            print("Unable to retrieve ticker data for {0} from {1}".format(symbol, self.name))
            return
        tradepair.exchange_name(self.name)
        tradepair.value = response.json()
        pass
