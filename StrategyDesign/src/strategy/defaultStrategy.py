from . import PasswordStrategyInterface

class DefaultPasswordStrategy(PasswordStrategyInterface):
    def generate(self):
        return 'abc_default_10'