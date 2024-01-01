from scroll import *
from player import *
from jackpotMachine import *
from icecream import ic

if __name__ == '__main__':
    start = 0
    end = 9
    scrolls = []
    for i in range(3):
        scroll = Scroll(start, end)
        scrolls.append(scroll)
    
    players = []
    for i in range(2):
        player = Player(f'Player {i+1}', 3)
        players.append(player)

    
    machine = JackpotMachine(scrolls, players)

    ic(machine.pullLever())
    ic(machine.pullLever())
    ic(machine.pullLever())
    ic(machine.pullLever())
    ic(machine.pullLever())
    ic(machine.pullLever())
    ic(machine.pullLever())
    