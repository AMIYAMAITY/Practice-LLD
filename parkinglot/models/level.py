from typing import List
from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle

class Level:
    def __init__(self, floor: int, num_spots : int):
        self.floor = floor
        self.parking_spots = List[ParkingSpot]
        self.parking_spots = [ParkingSpot(i) for i in range(num_spots)]
    
    def get_floor_number(self) -> int:
        return self.floor

    def park_vehicle(self, vehicle : Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and vehicle.type in spot.get_vehicle_types():
                spot.park_vehicle(vehicle)
                return True
        return False

    def unpark_vehicle(self, vehicle : Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.unpark_vehicle()
                return True
        return False
    


    def display_availability(self):
        available_count = 0
        occupied_count = 0
        for spot in self.parking_spots:
            if spot.is_available():
                available_count += 1 
            else:
                occupied_count += 1
        
        print("floor: ", self.get_floor_number(), "available_count: ", available_count, " occupied_count: ", occupied_count)