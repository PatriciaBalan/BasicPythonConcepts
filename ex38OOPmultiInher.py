#Battery and GPS Tracker: Create classes Battery and GPS with respective methods charge and location.
# Derive a SmartPhone class that inherits both functionalities.


class Battery():
    def charge(self):
        print("charging the battery")

class GPS():
    def location(self):
        print("current location is 123, 456")

class Smartphone(Battery, GPS):
    pass

phone = Smartphone()
phone.charge()
phone.location()