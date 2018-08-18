from .exchange import Exchange, TradePair


class CryptonatorExchange(Exchange):
    def __init__(self):
        super(CryptonatorExchange, self).__init__("Cryptonator", "https://api.cryptonator.com/api")
        pass

    def update(self):
        pass

    def update_tradepair(self, tradepair: TradePair):
        pass

