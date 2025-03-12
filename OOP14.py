class Electronics():
    def __init__(self, el_type):
        self.el_type = el_type

    def display(self):
        return self.el_type

class Laptop(Electronics):
    def __init__(self, el_type, display_det, processor, software):
        super().__init__(el_type)
        self.display_det = display_det
        self.processor = processor
        self.software = software

    def display(self):
        return f"{super().display()}, Display {self.display_det}, Processor {self.processor}, Software {self.software}"


class Phone(Electronics):
    def __init__(self, el_type, year, software, cams):
        super().__init__(el_type)
        self.year = year
        self.software = software
        self.cams = cams

    def display(self):
        return f"{super().display()}, Year {self.year}, Software {self.software}, Cams {self.cams}"

l = Laptop("laptop", 1400, "intel", "windows")
p = Phone("phone", 2024, "android", 2.2)
print(l.display())
print(p.display())