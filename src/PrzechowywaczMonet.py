from decimal import *
from exception.NiewlasciwaIloscMonet import NiewlasciwaIloscMonet


class PrzechowywaczMonet:
    _monety_dostepne_lista = ("0.01", "0.02", "0.05", "0.1", "0.2", "0.5", "1", "2", "5", "10", "20", "50")

    def __init__(self):
        self.lista_monet = []
        self.value = 0

    def addCoin(self, value, amount=1):
        if value in self._monety_dostepne_lista:
            self.value = Decimal(str(value))
            for i in range(amount):
                self.lista_monet.append(self.value)
        print(" wpłacono " + str(self.sumaMonet()))

    def sumaMonet(self):
        return Decimal(sum(self.lista_monet))

    def potwierdzIlosc(self, entry) -> int:
        '''metoda sprawdzająca, czy określona ilość monet została wprowadzona'''
        try:
            amount = int(entry)
            if (amount <= 0):
                raise NiewlasciwaIloscMonet()
            return amount
        except ValueError:
            raise NiewlasciwaIloscMonet()
