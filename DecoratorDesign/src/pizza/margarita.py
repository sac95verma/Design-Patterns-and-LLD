from .basePizzeInterface import IBasePizza

class Margarita(IBasePizza):
    def __init__(self):
        self.price = 100

    def getPrice(self):
        return self.price