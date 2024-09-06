
from models.vehicle import Vehicle
from models.vehicle_type import VehicleType

class Car(Vehicle):
    def __init__(self, license_plate: str) -> None:
        super().__init__(license_plate, VehicleType.CAR)