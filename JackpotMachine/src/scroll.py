import random
from icecream import ic

class Scroll:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def pullScrollLever(self):
        number = random.randint(self.start, self.end)
        return number