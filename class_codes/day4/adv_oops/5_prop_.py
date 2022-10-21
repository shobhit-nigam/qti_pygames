class Sample:
    def __init__(self, varx):
        self.__set_varx(varx)

    def __get_varx(self):
        print("getting object....")
        return self.__varx

    def __set_varx(self, varx):
        print("setting object .....")
        if varx < 0:
            self.__varx = 0
        elif varx > 100:
            self.__varx = 100
        else:
            self.__varx = varx

    varx = property(__get_varx, __set_varx)

obja = Sample(-111)
objb = Sample(12)

print(obja.varx)
obja.varx = 600

print(obja.varx)
