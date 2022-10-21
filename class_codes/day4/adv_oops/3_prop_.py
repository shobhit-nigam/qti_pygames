class Sample:
    def __init__(self, varx):
        self.set_varx(varx)

    def get_varx(self):
        return self.__varx

    def set_varx(self, varx):
        if varx < 0:
            self.__varx = 0
        elif varx > 100:
            self.__varx = 100
        else:
            self.__varx = varx

    varx = property(get_varx, set_varx)

obja = Sample(11)
objb = Sample(12)

obja.set_varx(-100)
objb.set_varx(143)

obja.varx = 600

print(obja.varx)
