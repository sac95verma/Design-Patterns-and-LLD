
class BaseException(Exception):
    def __init__(self):
        super().__init__(f'Some internal error occurred')

class ParkingFullException(Exception):
    def __init__(self, vehicleType):
        super().__init__(f'There are no parking slots for {vehicleType}')
        self.vehicleType = vehicleType

class TicketInvalidException(Exception):
    def __init__(self, ticket):
        super().__init__(f'The ticket number: {ticket} is invalid')
        self.ticket = ticket

class ParkingSpaceOccupiedException(Exception):
    def __init__(self):
        super().__init__(f'The parking space is already occupied and can\'t be removed')