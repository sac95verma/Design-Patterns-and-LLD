from .toppingDecorator import IToppingDecorator
from ..basePizzeInterface import IBasePizza

class ExtraOnion(IToppingDecorator):

    def __init__(self, pizza: IBasePizza):
        self.pizza = pizza
    
    def getPrice(self):
        return self.pizza.getPrice()+ 50