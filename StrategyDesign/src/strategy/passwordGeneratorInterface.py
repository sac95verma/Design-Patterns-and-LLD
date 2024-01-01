from abc import ABC

class PasswordStrategyInterface(ABC):

    # def __init__(self, length):
    #     self.length = length

    def generate(self):
        pass