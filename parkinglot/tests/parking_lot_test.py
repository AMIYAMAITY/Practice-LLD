from src.parking_lot import ParkingLot
from models.level import Level
from models.types.car import Car
from models.types.truck import Truck
from models.types.motorbike import MotorBike 


class ParkingLotTest:
    def run(self):
        parkingLotObj = ParkingLot.get_instance()
        parkingLotObj.display_availability()

        parkingLotObj.add_level(Level(1,10)) #floor, spot/cell number
        parkingLotObj.add_level(Level(2,15)) #floor, spot/cell number

        try:
            parkingLotObj.add_level(Level(1,8)) #floor, spot/cell number
        except Exception as ex:
            print(ex)

        # park
        car  = Car("WB34U3214")
        motorbike  = MotorBike("WB34U3314")
        truck  = Truck("WB34U3315")
        print(parkingLotObj.park_vehicle(car))
        print(parkingLotObj.park_vehicle(motorbike))
        print(parkingLotObj.park_vehicle(truck))

        parkingLotObj.display_availability()
        parkingLotObj.unpark_vehicle(motorbike)
        parkingLotObj.display_availability()

        # should give same availibility, because truck is not in the default vehicle type in each spot.
        parkingLotObj.display_availability()
        parkingLotObj.unpark_vehicle(truck)
        parkingLotObj.display_availability()



if __name__ == '__main__':
    parkingLotTestObj = ParkingLotTest()
    parkingLotTestObj.run()