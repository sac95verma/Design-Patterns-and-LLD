from ParkingLot import ParkingLot
from ParkingSpace import CarParking, BikeParking, TruckParking
from VehicleInterface import Car, Bike, Truck
from icecream import ic

if __name__ == '__main__':
    # create parking spaces

    parkingSpaces = []
    totalSize = 18
    i = 0
    while i < totalSize:
        if i < 10:
            parkingSpace = CarParking(i)
        elif i< 15:
            parkingSpace = BikeParking(i)
        else:
            parkingSpace = TruckParking(i)
        i+=1
        parkingSpaces.append(parkingSpace)

    parkingLot = ParkingLot('P1')

    parkingLot.addParkingSlots(parkingSpaces)

    # createVehicle

    car1 = Car('red', 'KA1009')
    car2 = Car('blue', 'KA1001')

    ticket1 = parkingLot.parkVehicle(car1)
    ticket2 = parkingLot.parkVehicle(car2)
    ic(ticket1)
    ic(ticket2)
    ic(parkingLot.occupancy)

    ic(parkingLot.getVehicle(ticket1+ticket2))