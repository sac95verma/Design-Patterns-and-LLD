import random
import string
from . import PasswordStrategyInterface

class AlphaNumericPasswordStrategy(PasswordStrategyInterface):
    def __init__(self, length):
        self.length = length

    def generate(self):
        def random_alphanumeric(length =10):
            """Generates a random alphanumeric string of specified length."""
            letters_and_digits = string.ascii_letters + string.digits
            return ''.join(random.choice(letters_and_digits) for _ in range(length))
        
        return random_alphanumeric(self.length)