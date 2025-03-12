class Person():
    def __init(self, name, age):
        self._name= name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_age(self, a):
        self._age = a

p = Person()
p.set_age(21)
print(p.get_age())