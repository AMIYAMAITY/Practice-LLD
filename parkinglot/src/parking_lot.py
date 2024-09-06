
from typing import List
from models.level import Level
from models.vehicle import Vehicle

class ParkingLot:
    _instance= None

    def __init__(self) -> None:
        if ParkingLot._instance is not None:
            raise Exception("This class is singleton")
        else:
            ParkingLot._instance = self
            self.levels = []
    
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        
        return ParkingLot._instance
    
    def add_level(self, level : Level):
        for curr_level in self.levels:
            if curr_level.get_floor_number() == level.get_floor_number():
                raise ValueError(level.get_floor_number(), " This floor is already added")

        self.levels.append(level)

    def park_vehicle(self, vehicle : Vehicle) -> bool:
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False
    
    def unpark_vehicle(self, vehicle : Vehicle) -> bool:
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False
    
    def display_availability(self):
        for level in self.levels:
            level.display_availability()

    
