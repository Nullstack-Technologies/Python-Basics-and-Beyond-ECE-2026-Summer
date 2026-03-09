class Vehicle:

    def __init__(self, wheels, brand, vehicle_type):
        self.wheels = wheels
        self.brand = brand
        self.vehicle_type = vehicle_type
    
    def __add__(self, b):
        return self.wheels + b.wheels

    def details(self):
        print(f"Vehicle: {self.brand} {self.wheels} wheeler ({self.vehicle_type})")

    def accelerate(self):
        print("Accelerating")

a = Vehicle(wheels=4, brand="Skoda", vehicle_type="EV")
b = Vehicle(wheels=2, brand="Royal Enfield", vehicle_type="Petrol Car")
# a.details()
# b.details()

print(a + b)