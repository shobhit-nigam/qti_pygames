class Sample:
    datax = 100

    def method_a(self, val):
        self.datax = val

    @staticmethod
    def method_b():
        print("in static method")


objp = Sample()
objq = Sample()
objp.method_b()
