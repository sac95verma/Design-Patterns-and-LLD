from .basePizzeInterface import IBasePizza

class ChickenSupreme(IBasePizza):
    def __init__(self):
        self.price = 150

    def getPrice(self):
        return self.price