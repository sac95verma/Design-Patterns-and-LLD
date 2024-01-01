from ParkingSpace import CarParking, BikeParking, TruckParking, IParkingSpace
from VehicleInterface import IVehicle
from ticket import Ticket
from utils import VehicleType
from icecream import ic
from exceptions.exceptions import *

class ParkingLot:

    def __init__(self, parkingLotId):
        self.parkingLotId = parkingLotId
        self.parkingSpaces = {}
        self.occupancy = {
            VehicleType.CAR : 0,
            VehicleType.BIKE : 0,
            VehicleType.TRUCK : 0,
            'totalSlots' : 0,
        }
        self.ticket = Ticket()

    
    def addParkingSlots(self, parkingSpaces: list[IParkingSpace]):
        for parkingSpace in parkingSpaces:
            self.parkingSpaces[parkingSpace.slotId] = parkingSpace
            self.updateOccupancy(parkingSpace)
        return

    def updateOccupancy(self, parkingSpace: IParkingSpace):
        self.occupancy[parkingSpace.slotType] +=1
        self.occupancy['totalSlots'] +=1

    def removeParkingSlot(self, parkingSpace: IParkingSpace):
        if parkingSpace.slotId in self.parkingSpaces and parkingSpace.isVacant:
            del(self.parkingSpaces[parkingSpace.slotId])
            self.occupancy[parkingSpace.slotType] -=1
            self.occupancy['totalSlots'] -=1
        else:
            raise ParkingSpaceOccupiedException()

    def parkVehicle(self, vehicle: IVehicle):
        try:
            availableParkingSpace = self.getAvailableSlot(vehicle.type)
            if availableParkingSpace:
                slotId = availableParkingSpace.park(vehicle)
                ic(slotId)
                self.occupancy[vehicle.type] -= 1
                return self.ticket.generateTicket(self.parkingLotId, slotId, vehicle.registrationNumber)
        except ParkingFullException as e:
            print(e)

    def getAvailableSlot(self, vehicleType):
        if self.occupancy[vehicleType] == 0:
            raise ParkingFullException(vehicle.type)
        for key, parkingObj in self.parkingSpaces.items():
            if parkingObj.slotType == vehicleType and parkingObj.isVacant:
                return parkingObj
        raise ParkingFullException(vehicle.type)

    def getVehicle(self, ticket):
        try:
            if self.ticket.validateTicket(ticket):
                return self.unparkVehicle(ticket)
        except TicketInvalidException as e:
            ic(e)

    def unparkVehicle(self, ticket):
        try:
            slotId = self.ticket.getParkinDetails(ticket)
            parkingSpace = self.parkingSpaces.get(int(slotId), None)
            if parkingSpace:
                self.occupancy[parkingSpace.slotType] += 1
                return parkingSpace.unparkVehicle()
        except BaseException as e:
            ic(e.value)    