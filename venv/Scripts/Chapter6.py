class Vehicle: pass
class Vehicle: engine_capacity = "1,6 Turbo"
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capcity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def Drive(self):print("This vehicle is in driving mode now.")

class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels,'eletric', seating_capacity, maximum_velocity)

vios = Vehicle ('4','petrol', 5, 180)
print(vios.number_of_wheels)
print(vios.type_of_tank)
print(vios.seating_capcity)
print(vios.maximum_velocity)
vios.Drive()

blueSG = ElectricCar('4', 5, 150)
print(blueSG.type_of_tank)
blueSG.Drive()