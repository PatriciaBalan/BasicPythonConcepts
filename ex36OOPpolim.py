#Polymorphism with a Function: Create a function describe_pet that takes an object of
# Animal and calls its speak method, demonstrating polymorphism.

class Animal():
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog():
    def speak(self):
        print("Woaf")

class Cat():
    def speak(self):
        print("Meouw")

class Parrot(Animal):
    def speak(self):
        print("Squawk!")

def describe_pet(animal):
    animal.speak()


dog = Dog()
cat = Cat()
parrot = Parrot()

describe_pet(dog)
describe_pet(cat)
describe_pet(parrot)


