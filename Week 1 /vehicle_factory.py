class Car:
    def drive(self):
        print("Driving a Car")


class Bike:
    def drive(self):
        print("Riding a Bike")


class Truck:
    def drive(self):
        print("Driving a Truck")


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):

        if vehicle_type.lower() == "car":
            return Car()

        elif vehicle_type.lower() == "bike":
            return Bike()

        elif vehicle_type.lower() == "truck":
            return Truck()

        else:
            return None


vehicle = VehicleFactory.get_vehicle("car")

if vehicle:
    vehicle.drive()
else:
    print("Invalid Vehicle")
