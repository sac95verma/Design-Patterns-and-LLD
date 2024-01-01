from passwordGenerator import PasswordGenerator
from strategy import AlphaNumericPasswordStrategy
from strategy import DefaultPasswordStrategy

def getPassword(length):
    password = PasswordGenerator()
    p = password.generatePassword(AlphaNumericPasswordStrategy(length))
    print(p)
    return p

if __name__ == '__main__':
    getPassword(10)