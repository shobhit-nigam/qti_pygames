class Sample:
    def __init__(self, varx):
        self.varx = varx

    @property
    def varx(self):
        print("getting object....")
        return self.__varx

    @varx.setter
    def varx(self, varx):
        print("setting object .....")
        if varx < 0:
            self.__varx = 0
        elif varx > 100:
            self.__varx = 100
        else:
            self.__varx = varx

obja = Sample(-111)
objb = Sample(12)

print(obja.varx)
obja.varx = 600

print(obja.varx)
