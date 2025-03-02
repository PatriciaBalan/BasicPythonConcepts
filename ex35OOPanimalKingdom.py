#Inheritance - Animal Kingdom: Create a base class Animal with a method speak().
# Derive two classes Dog and Cat from Animal and override the speak method to reflect their sounds.

class Animal():
    def speak(self):
        pass

class Dog():
    def speak(self):
        print("Woaf")

class Cat():
    def speak(self):
        print("Meouw")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()