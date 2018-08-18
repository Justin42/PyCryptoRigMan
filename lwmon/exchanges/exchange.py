from collections import namedtuple
from typing import List
from abc import ABC, abstractmethod

TradePair = namedtuple("TradePair", "exchange_name coin1 coin2 value altvalues")


class Exchange(ABC):
    def __init__(self, name: str, endpoint: str):
        self.name = name
        self.tradepairs: List[TradePair] = []
        self.endpoint = endpoint
        if self.endpoint.endswith("/"):
            self.endpoint = self.endpoint[:-1]

    @abstractmethod
    def update(self):
        for pair in self.tradepairs:
            self.update_tradepair(pair)
            pass

    @abstractmethod
    def update_tradepair(self, tradepair: TradePair):
        if tradepair not in self.tradepairs:
            pass
        else:
            pass

    def add_tradepair(self, tradepair: TradePair):
        if tradepair not in self.tradepairs:
            key = "{0}-{1}".format(tradepair.coin1, tradepair.coin2)
            self.tradepairs[key] = tradepair

    def get_tradepair(self, coin1: str, coin2: str):
        return self.tradepairs.get("{0}-{1}".format(coin1, coin2))

    def convert(self, coin1, coin2, amount) -> int:
        found_pair = False
        for pair in self.tradepairs:
            if pair.coin1 == coin1 and pair.coin2 == coin2:
                found_pair = pair
        if found_pair:
            return found_pair.value * amount
        return 0
