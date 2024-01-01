from abc import ABC
from utils import VehicleType

class IVehicle(ABC):

    def __init__(self):
        pass

class Car(IVehicle):

    def __init__(self, color, registrationNumber):
        self.type = VehicleType.CAR
        self.color = color
        self.registrationNumber = registrationNumber


class Bike(IVehicle):

    def __init__(self, color, registrationNumber):
        self.type = VehicleType.BIKE
        self.color = color
        self.registrationNumber = registrationNumber
        

class Truck(IVehicle):

    def __init__(self, color, registrationNumber):
        self.type = VehicleType.TRUCK
        self.color = color
        self.registrationNumber = registrationNumber
        