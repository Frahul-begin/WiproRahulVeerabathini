class Vehicle:
    vehicle_count = 0
    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started")

class EVCar(Car):
    def start(self):
        print("EV Car started")

v = Vehicle()
c = Car()
e = EVCar()

v.start()
c.start()
e.start()

print("Total vehicle count: ", Vehicle.vehicle_count)
