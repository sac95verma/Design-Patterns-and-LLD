from strategy import PasswordStrategyInterface

class PasswordGenerator:
    def generatePassword(self, strategy: PasswordStrategyInterface):
        password = strategy.generate()
        return password
