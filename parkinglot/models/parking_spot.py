from models.vehicle_type import VehicleType
from models.vehicle import Vehicle
from threading import *
l=Lock()

class ParkingSpot:
    def __init__(self, spot_number : int) -> None:
        self.spot_number = spot_number
        self.vehicle_types = set([VehicleType.CAR, VehicleType.MOTORBIKE])
        self.parked_vehicle = None
    
    def get_vehicle_types(self) -> set:
        return set(self.vehicle_types)

    def is_available(self):
        return self.parked_vehicle == None
    
    def park_vehicle(self, vehicle : Vehicle):
        l.acquire()
        if self.is_available() and vehicle.type in self.vehicle_types:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("Invalid vehicle type or spot is already occupied")
        l.release()
    
    def unpark_vehicle(self):
        l.acquire()
        self.parked_vehicle = None
        l.release()

    def get_vehicle_type(self) -> VehicleType:
        if not self.is_available():
            return self.parked_vehicle.get_vehicle_type()
        else:
            raise ValueError("Spot is empty")

    def get_parked_vehicle(self) -> Vehicle:
        if not self.is_available():
            return self.parked_vehicle

        raise ValueError("Spot is empty")
    
    def get_spot_number(self) -> int:
        return self.spot_number
