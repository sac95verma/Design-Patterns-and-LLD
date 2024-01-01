from pizza.chickenSupreme import ChickenSupreme
from pizza.margarita import Margarita
from pizza.toppingDecorators.cheeseTopping import CheeseTopping
from pizza.toppingDecorators.extraOnion import ExtraOnion

def makePizza():
    pizza =  CheeseTopping(ExtraOnion(ChickenSupreme()))
    price = pizza.getPrice()
    print(price)
    return price

if __name__ == '__main__':
    makePizza()