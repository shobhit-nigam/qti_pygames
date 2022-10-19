class Sample:
    datax = 100

    def method_a(self, val):
        self.datax = val

    def display(self):
        print(f"datax = {self.datax}")

objp = Sample()
objq = Sample()
#objp.datax = 50
#objq.datax = 60

print(f"datax for objp is {objp.datax}")
objp.method_a(55)
print("-"*10)
print(f"datax for objp is {objp.datax}")
print("-"*10)
print(f"datax for objq is {objq.datax}")
Sample.datax = 111
print("-"*10)
print(f"datax for Sample is {Sample.datax}")
print("-"*10)
print(f"datax for objp is {objp.datax}")
print("-"*10)
print(f"datax for objq is {objq.datax}")
