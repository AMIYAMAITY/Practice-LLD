from models.vehicle_type import VehicleType

class Vehicle:
    def __init__(self, license_plate : str, vehicle_type : VehicleType) -> None:
        self.license_plate = license_plate
        self.type = vehicle_type
    
    def get_vehicle_type(self) -> VehicleType:
        return self.type
    
    def get_vehicle_LP(self) -> str:
        return self.license_plate