from abc import ABC, abstractmethod
from utils import VehicleType
from VehicleInterface import IVehicle
from icecream import ic

class IParkingSpace(ABC):

    def unparkVehicle(self):
        self.isVacant = True
        return 'Successfully retrieved'

    def park(self, vehicle: IVehicle):
        self.isVacant = False
        self.parkedVehicleNumber = vehicle.registrationNumber
        return self.slotId

class CarParking(IParkingSpace):

    def __init__(self, slotId):
        self.slotType = VehicleType.CAR
        self.slotId = slotId
        self.isVacant = True
        self.parkedVehicleNumber = None
    
    def park(self, vehicle: IVehicle):
        return super().park(vehicle)
    
    def unparkVehicle(self):
        return super().unparkVehicle()
    # def unparkVehicle(self):
    #     self.isVacant = True
    #     return 'Successfully retrieved'

class BikeParking(IParkingSpace):

    def __init__(self, slotId):
        self.slotType = VehicleType.BIKE
        self.slotId = slotId
        self.isVacant = True
        self.parkedVehicleNumber = None

    def park(self, vehicle: IVehicle):
        return super().park(vehicle)

    def unparkVehicle(self):
        return super().unparkVehicle()
    # def unparkVehicle(self):
    #     self.isVacant = True
    #     return 'Successfully retrieved'

class TruckParking(IParkingSpace):

    def __init__(self, slotId):
        self.slotType = VehicleType.TRUCK
        self.slotId = slotId
        self.isVacant = True
        self.parkedVehicleNumber = None
    
    def park(self, vehicle: IVehicle):
        return super().park(vehicle)

    def unparkVehicle(self):
        return super().unparkVehicle()
    # def unparkVehicle(self):
    #     self.isVacant = True
    #     return 'Successfully retrieved'