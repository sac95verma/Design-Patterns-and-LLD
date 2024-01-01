from exceptions.exceptions import *

class Ticket:

    def __init__(self):
        pass

    def generateTicket(self, parkingLotId, slotId, registrationNumber):
        return f'{parkingLotId}:{slotId}:{registrationNumber[:-4]}'

    def validateTicket(self, ticket):
        if len(ticket.split(':')) == 3:
            return True
        raise TicketInvalidException(ticket)

    def getParkinDetails(self, ticket):
        t = ticket.split(':')
        return t[1]