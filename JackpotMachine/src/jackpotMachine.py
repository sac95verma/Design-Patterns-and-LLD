from scroll import *
from player import *
from collections import Counter
from icecream import ic

class JackpotMachine:

    def __init__(self, scrolls: list[Scroll], players: list[Player]):
        self.scrolls = scrolls
        self.players = players
        self.turn = 0
        self.winner = None
    
    def pullLever(self):
        player = self.players[self.turn]

        if self.winner is not None:
            ic(f'Game already over. Player: {self.winner.getName()} already hit the jackpot')

        if player.getChancesLeft() == 0:
            ic(f'No chances left')
        
        res = [scroll.pullScrollLever() for scroll in self.scrolls]
        ic(f'Got : {res}')

        isWinner = self.checkWinner(player, res)
        if isWinner:
            ic(f'Player: {player.getName()} has hit the jackpot')
        else:
            player.decrementChancesByOne()
            self.turn = (self.turn + 1)%len(self.players)
        

    def checkWinner(self, player: Player, res: list):
        count = Counter(res)
        for num, freq in count.items():
            if freq == 3 or freq == 2:
                self.winner = player
                return True
        return False