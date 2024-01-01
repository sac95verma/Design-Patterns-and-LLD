
class Player:
    def __init__(self, name, chances):
        self.name = name
        self.chances = chances

    def getName(self):
        return self.name

    def getChancesLeft(self):
        return self.chances

    def decrementChancesByOne(self):
        self.chances-=1
        return