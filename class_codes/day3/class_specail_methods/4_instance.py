class Sample:
    datax = 100

    def method_a(self, val):
        self.datax = val

    @classmethod
    def method_b(self, val):
        self.datax = val


objp = Sample()
objq = Sample()

print(f"datax for objp is {objp.datax}")
objp.method_a(55)
print("-"*10)
print(f"datax for objp is {objp.datax}")
print("-"*10)
print(f"datax for objq is {objq.datax}")
objp.method_b(111)
print("-"*10)
print(f"datax for Sample is {Sample.datax}")
print("-"*10)
print(f"datax for objp is {objp.datax}")
print("-"*10)
print(f"datax for objq is {objq.datax}")

objr = Sample()
print("-"*10)
print(f"datax for objr is {objr.datax}")
