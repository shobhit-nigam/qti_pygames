class Parent:
    def __init__(self, x, y):
        self.varx = x
        self.vary = y

class Child(Parent):
    def __init__(self, x, y, z):
        Parent.__init__(self, x, y)
#        super().__init__(x, y)
        self.varz = z

    def display(self):
        print(f"varx = {self.varx}")
        print(f"vary = {self.vary}")
        print(f"varz = {self.varz}")

objl = Child(11, 22, 33)
objl.display()
