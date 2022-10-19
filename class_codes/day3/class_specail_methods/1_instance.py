class Sample:
    datax = 100

    def method_a(self, val):
        self.datax = val


    def method_b(self, val):
        self.datax = val

    def method_c():
        print("in method c")

    def display(self):
        print(f"datax = {self.datax}")

objp = Sample()
objq = Sample()
objr = Sample()

objp.display()
objp.method_a(77)
print("-"*10)
objp.display()
print("-"*10)
objq.display()
