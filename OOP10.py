from idlelib.tree import wheel_event


class Vechicle():
    def __init__(self, wheels, speed):
        self.wheels = wheels
        self.speed = speed

    def display(self):
        print(self.wheels, self.speed)

class Car(Vechicle):
    def __init__(self, model, wheels, speed):
        self.model = model # new property
        super().__init__(wheels, speed) # class parent prop
        self.wheels = wheels
        self.speed = speed

class Bike(Vechicle):
    def __init__(self, wheels, speed):
        super().__init__(wheels, speed)
        self.wheels = wheels
        self.speed = speed

    def print(self):
        print("bike class is calling")

v = Vechicle("4", 250)
print(v.speed, v.wheels)
c = Car("Toyota", 4, 200)
print(c.model)
b = Bike(2, 30)
print(b.speed)
print(b.wheels)



#class Bike(Vechicle):